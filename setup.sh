#!/bin/bash

#update system
sudo yum -y update && upgrade

#install git python and devtools
sudo yum -y install git-all centos-relese-SCL python-setuptools python-setuptools-devel python-devel
sudo yum -y groupinstall "Development Tools"

#install pip
sudo easy_install pip

#clone proejct repo
git clone https://github.com/mishapapasha/SCE-2018-Elections.git
cd SCE-2018-Elections

#install our app requirements
sudo pip install -r requirements.txt

#create db
python db_create.py

#redirects all traffic from port 80 to 5000
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000

#run app
nohup python run.py > ../log.txt 2>&1 </dev/null &

