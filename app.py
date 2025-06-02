import boto3

def get_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    return response


if __name__ == "__main__":
    instances = get_ec2_instances()
    print(f"EC2 Instances: {instances}")