import boto3

def launch_instance():
    ec2 = boto3.client("ec2")
    response = ec2.run_instances(
        ImageId="ami-019715e0d74f695be",
        InstanceType="t3.micro",
        KeyName="python8am",
        MinCount=1,
        MaxCount=1
    )
    instance_id = response["Instances"][0]["InstanceId"]
    print(f"Instance launched: {instance_id}")
    print("Waiting for instance to start")
    waiter = ec2.get_waiter("instance_running")
    waiter.wait(InstanceIds=[instance_id])
    print("Instance running successfully!")
    description = ec2.describe_instances(InstanceIds=[instance_id])
    public_ip = description["Reservations"][0]["Instances"][0]["PublicIpAddress"]
    print(f"Public IPV4: {public_ip}")

launch_instance()