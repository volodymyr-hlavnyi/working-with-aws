import boto3
import os
from os import environ as env
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def get_credentials():
    aws_access_key_id = env.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = env.get("AWS_SECRET_ACCESS_KEY")

    return {
        "aws_access_key_id": aws_access_key_id,
        "aws_secret_access_key": aws_secret_access_key
    }


def get_session():
    credentials = get_credentials()
    session = boto3.Session(
        aws_access_key_id=credentials['aws_access_key_id'],
        aws_secret_access_key=credentials['aws_secret_access_key'],
        region_name=env.get("AWS_REGION", "us-east-1")
    )
    return session


def get_ec2_instances():
    session = get_session()
    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    return response


def get_s3_buckets():
    session = get_session()
    s3 = session.client('s3')
    response = s3.list_buckets()
    return response


def get_users():
    session = get_session()
    iam = session.client('iam')
    response = iam.list_users()
    return response


if __name__ == "__main__":
    instances = get_ec2_instances()
    print(f"EC2 Instances: {instances}")

    buckets = get_s3_buckets()
    print(f"S3 Buckets: {buckets['Buckets'] if 'Buckets' in buckets else 'No buckets found'}")

    users = get_users()
    print(f"IAM Users: {users['Users'] if 'Users' in users else 'No users found'}")