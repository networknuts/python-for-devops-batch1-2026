import os
import boto3

def walking(parent_path,bucket_name):
    s3 = boto3.client("s3")
    print(f"Starting directory walk in {parent_path}")
    children = os.listdir(parent_path)
    for child in children:
        child_path = os.path.join(parent_path,child) #/home/aryan/.ssh /home/aryan - parent, .ssh - child
        if os.path.isfile(child_path):
                s3.upload_file(child_path,bucket_name,child)
                print(f"{child} ---> {bucket_name}")
        elif os.path.isdir(child_path):
            pass


parent_path = input("Enter main directory: ")
bucket_name = input("Enter bucket name: ")
walking(parent_path,bucket_name)