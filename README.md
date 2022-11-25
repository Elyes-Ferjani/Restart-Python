# Restart-Python


## Create an s3 bucket <your.name>-20221125
example John-20221125

## create a role and add permission ( S3 full access )
go to IAM, Create IAM role and attach S3 full Access permissions to the role

## attach the role to the EC2 instance
click on action => security => edit IAM role

## open port 8080 (SG)
Check the security group associated with the EC2 ENI

## SSH to the instance
ssh -i <keyname> ec2-user@<public-ip>

## If you dont have pip installed, then install pip
sudo yum install epel-release -y;
sudo yum install python-pip -y

## Install Git
sudo yum install git -y

## clone flask project
git clone https://github.com/Elyes-Ferjani/Restart-Python.git

## you need to run flask application
cd Restart-Python

## Install virtualenv
python3 -m pip install --user virtualenv


## create a virtual environment
python3 -m venv env

## activate the environment
source env/bin/activate

## You need to install flask and boto3
pip install flask;
pip install boto3

## Run the application
python3 server.py <your.name>-20221125

## Test the application
go to browser hit : http://ec2-public-ip:8080/