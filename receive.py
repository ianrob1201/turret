import json
import boto3
import sys
import yaml
from time import sleep
from firebase import firebase
import serial


firebase = firebase.FirebaseApplication('https://turret-a2f8e.firebaseio.com/', None)

def sendCommand(command):
    ser.write(command + "\n")

def getValue(name, field):
    result = firebase.get('/people', None)
    jsonResult = yaml.load(json.dumps(result))
    for x in jsonResult:
        if x['name'].upper() == name.upper():
            return x[field]
    return 90

def rotate(json):
    pan = getValue(json.loads(message.body)['name'], 'pan')
    tilt = getValue(json.loads(message.body)['name'], 'tilt')
    # Print out the body and author (if set)
    print(pan)
    print(tilt)
    rotate = "ROTATE:" + pan + ":" + tilt
    print(rotate)
    sendCommand(rotate)
    sleep(1)

def shoot():
    sendCommand("SHOOT")
    sleep(1)

def centre():
    sendCommand("ROTATE:90:90")



ser = serial.Serial('/dev/ttyUSB0', 9600)
print(ser.name)
print(ser.readline())
# sendCommand('LASER')

# sys.exit()

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='turret')

print('Checking for messages. Ctrl-C to exit...')
while (True):
    # Process messages by printing out body and optional author name
    for message in queue.receive_messages(MessageAttributeNames=['Author']):      
        command = json.loads(message.body)['command'].upper()
        if (command == 'SHOOT'):
            rotate(json)
            shoot()
            centre()
        elif (command == 'AIM' ):
            rotate(json)
        elif (command == 'CUSTOM' ):
            sendCommand(json.loads(message.body)['customCommand'].encode('ascii','ignore'))
        # Let the queue know that the message is processed
        message.delete()