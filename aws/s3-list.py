import boto3

def list_buckets():
    s3 = boto3.client("s3")

    response = s3.list_buckets()
    n = 0
    for bucket in response['Buckets']:
        n = n + 1
        print(f"{n}. {bucket['Name']}")
    print(f"\nTotal Buckets: {n}")

list_buckets()