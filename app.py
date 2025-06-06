import datetime
import json

import boto3
import os
from os import environ as env
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

BASEDIR = os.path.abspath(os.path.dirname(__file__))


# Custom JSON encoder to handle datetime objects
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO 8601 string
        return super().default(obj)


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

    if session is None:
        print("Failed to create AWS session EC2.")
        return None

    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    return response


def get_s3_buckets():
    session = get_session()
    if session is None:
        print("Failed to create AWS session S3.")
        return None

    s3 = session.client('s3')
    response = s3.list_buckets()
    return response


def get_cloudwatch_metrics():
    session = get_session()
    if session is None:
        print("Failed to create AWS session CloudWatch.")
        return None

    cloudwatch = session.client('cloudwatch')
    response = cloudwatch.list_metrics()
    return response


def get_users():
    session = get_session()
    if session is None:
        print("Failed to create AWS session IAM.")
        return None

    iam = session.client('iam')
    response = iam.list_users()
    return response


def print_response(response):
    if response is None:
        print("No data found or error retrieving data.")
        return

    if isinstance(response, dict):
        print(json.dumps(response, indent=4, cls=CustomJSONEncoder))
    elif isinstance(response, list):
        print(json.dumps(response, indent=4, cls=CustomJSONEncoder))
    else:
        print("Unsupported response type.")


if __name__ == "__main__":
    print("Welcome to the AWS CLI Tool")

    while True:
        print("\nSelect an option:")
        print("1. EC2 Instances")
        print("2. S3 Buckets")
        print("3. IAM Users")
        print("4. CloudWatch Metrics")
        print("9. Exit")
        answer = input("Select aws service: ").strip().lower()
        if answer == '9':
            print("Exiting the AWS CLI Tool.")
            break
        elif answer == '1':
            instances = get_ec2_instances()
            print_response(instances)
        elif answer == '2':
            buckets = get_s3_buckets()
            print_response(buckets)
        elif answer == '3':
            users = get_users()
            print_response(users)
        elif answer == '4':
            metrics = get_cloudwatch_metrics()
            print_response(metrics)
