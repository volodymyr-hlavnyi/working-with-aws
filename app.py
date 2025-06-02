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
    session = None
    try:
        session = boto3.Session(
            aws_access_key_id=credentials['aws_access_key_id'],
            aws_secret_access_key=credentials['aws_secret_access_key'],
            region_name=env.get("AWS_REGION", "us-east-1")
        )
    except Exception as e:
        print(f"Error creating AWS session: {e}")

    return session


def get_ec2_instances():
    session = get_session()
    if not session:
        ec2 = session.client('ec2')
        response = ec2.describe_instances()
        return response
    print("Failed to create AWS session.")
    return None


def get_s3_buckets():
    session = get_session()
    if not session:
        s3 = session.client('s3')
        response = s3.list_buckets()
        return response
    print("Failed to create AWS session.")
    return None


def get_users():
    session = get_session()
    if not session:
        iam = session.client('iam')
        response = iam.list_users()
        return response
    print("Failed to create AWS session.")
    return None


if __name__ == "__main__":
    instances = get_ec2_instances()
    if instances:
        print(f"EC2 Instances: {instances}")
    else:
        print("No EC2 instances found or error retrieving instances.")


    buckets = get_s3_buckets()
    if buckets:
        print(f"S3 Buckets: {buckets['Buckets'] if 'Buckets' in buckets else 'No buckets found'}")
    else:
        print("No S3 buckets found or error retrieving buckets.")

    users = get_users()
    if users:
        print(f"IAM Users: {users['Users'] if 'Users' in users else 'No users found'}")
    else:
        print("No IAM users found or error retrieving users.")