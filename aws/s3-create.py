import boto3

def create_bucket(bucket_name, bucket_region='ap-south-1'):
    client = boto3.client('s3')
    try:
        response = client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint':bucket_region
                }
            )
        print("Bucket created successfully!")
        print(f"Name: {bucket_name}")
        print(f"URL: {response['Location']}")
        print(f"Region: {bucket_region}")
    except Exception as e:
        print(f"Error: {e}")

create_bucket("networknuts-python-3")