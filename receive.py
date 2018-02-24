import json
import boto3
import usb.core
import usb.util
from firebase import firebase

firebase = firebase.FirebaseApplication('https://turret-a2f8e.firebaseio.com/', None)

def getRotation(name):
    result = firebase.get('/people', None)
    matches = [x for x in result if x['name']==name]
    return matches[0]['rotation']

def setupUsb():
    dev = usb.core.find(idVendor=0x0403, idProduct=0x6001)
    dev.set_configuration()
    cfg = dev.get_active_configuration()
    intf = cfg[(0,0)]

    ep = usb.util.find_descriptor(
        intf,
        # match the first OUT endpoint
        custom_match = lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT)

    assert ep is not None
    ep.write('LASER')

setupUsb()

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='turret')

print('Checking for messages. Ctrl-C to exit...')
while (True):
    # Process messages by printing out body and optional author name
    for message in queue.receive_messages(MessageAttributeNames=['Author']):
        
        rotation = getRotation(json.loads(message.body)['name'])
        # Print out the body and author (if set)
        print('Set rotation to {0}'.format(rotation))

        # Let the queue know that the message is processed
        message.delete()