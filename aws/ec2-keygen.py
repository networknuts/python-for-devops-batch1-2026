import boto3
import os

REGION = "ap-south-1"

def create_key_pair(key_name,key_file):
    ec2 = boto3.client("ec2",region_name=REGION)
    response = ec2.create_key_pair(KeyName=key_name)
    f = open(key_file,"w")
    f.write(response["KeyMaterial"])
    f.close()
    os.chmod(key_file, 0o400)
    print("key pair created and saved successfully!")

create_key_pair("python8am","python8am.pem")