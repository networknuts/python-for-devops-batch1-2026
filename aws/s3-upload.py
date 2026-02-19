import boto3

def upload_file(bucket_name,local_file,object_name=None):
    try:
        s3 = boto3.client("s3")
        if object_name is None:
            object_name = local_file
        s3.upload_file(local_file,bucket_name,object_name)
        print("Uploaded successfully!")
        print(f"{local_file} -----> {bucket_name}")
        print(f"Object Name: {object_name}")
    except Exception as e:
        print(f"Error: {e}")

upload_file("networknuts-python","/home/aryan/data.txt")