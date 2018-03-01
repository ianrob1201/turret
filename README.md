# turret2

> A Vue.js project

## Installation on Raspberry PI

* Start with base Raspian image (https://www.raspberrypi.org/downloads/raspbian/) installed onto the PI

* Run the following commands to install dependencies:

```
sudo pip install boto3
sudo pip install requests==1.1.0
sudo pip install python-firebase
sudo pip install pyyaml
sudo apt-get install socat

sudo pip install awscli
sudo aws configure -- Setup AWS API key, region = eu-west-1

curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs

sudo apt-get install apache2
sudo chmod a+w /var/www/html/
sudo chmod a+w /var/www/html/index.html
(Setup Git credentials)
git clone git@github.com:ianrob1201/turret.git
cd turret
npm install
npm run build
mkdir logs

# Setup crontab to run python listener script on reboot
sudo crontab -e
# Add line "@reboot sh /home/pi/turret/startup.sh >/home/pi/turret/logs/cronlog 2>&1" to end of file
```

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
