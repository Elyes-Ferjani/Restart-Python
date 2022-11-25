# Restart-Python
# Create an s3 bucket <your.name>-20221125
# create a role and add permission ( S3 full access )
# attach the role to the EC2 instance
# open port 8080 (SG)


# If you dont have pip installed, then install pip
sudo yum install epel-release
sudo yum install python-pip

# Install Git

sudo yum install git -y

# You need to install flask and boto3
pip install flask 
pip install boto3


# clone flask project

git clone https://github.com/Elyes-Ferjani/Restart-Python.git

# you need to run flask application
cd Restart-Python
python3 server.py <your.name>-20221125