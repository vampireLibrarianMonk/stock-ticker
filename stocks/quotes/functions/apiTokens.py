import boto3
import os

# loads function from json module as json_loads for parsing JSON strings into Python dictionaries.
from json import loads as json_loads

# Django's messaging framework for displaying temporary messages to the user.
from django.contrib import messages


def get_secret():
    # Attempt to retrieve the SECRET_TOKEN environment variable
    secret_token = os.getenv('SECRET_TOKEN')

    # Check if the environment variable exists
    if secret_token is not None:
        return secret_token
    else:
        print("SECRET_TOKEN does not exist falling back to AWS Secret Manager.")

        # Name of the secret you want to retrieve.
        secret_name = os.getenv("SECRET_NAME")

        # AWS region where your secret is stored.
        region_name = os.getenv("AWS_REGION")

        # Create a session using Boto3 library.
        session = boto3.session.Session()

        # Create a Secrets Manager client from the session.
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        # Use the client to retrieve the secret value.
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)

        # Return the actual secret value from the response.
        return json_loads(get_secret_value_response['SecretString'])['SECRET_TOKEN']

# Instructions for Setting Up AWS CLI and Running the Script
#
# 1. Install AWS CLI:
# Before running the script, ensure the AWS CLI is installed on your machine.
# Visit the AWS CLI installation guide for detailed instructions.
#
# 2. Configure AWS CLI:
# After installing the CLI, you need to configure it with your AWS credentials.
# Open your terminal and run:
#
# aws configure
#
# This command prompts you for:
#     AWS Access Key ID: Your access key.
#     AWS Secret Access Key: Your secret key.
#     Default region name: Your default AWS region, e.g., us-east-1.
#     Default output format: Preferred output format, e.g., json.
#
# Find or create your access key and secret key in the Management Console under your user profile in the IAM section.
#
# 3. Run the Script:
# With AWS CLI configured, run your Python script. Ensure your AWS user or role
# has the necessary permissions to access Secrets Manager, specifically secretsmanager:GetSecretValue.
#
# 4. Required Permissions:
# Ensure the IAM role or user executing the script has permissions to access Secrets Manager.
# Attach a policy like SecretsManagerReadWrite or create a custom policy that allows secretsmanager:GetSecretValue.
#
# Additional Resources:
#     Learn more about Boto3 and AWS SDK for Python in the Boto3 Documentation.
#     Dive deeper into AWS Secrets Manager by visiting the AWS Secrets Manager Documentation.
#
# This setup provides a comprehensive overview. Depending on specific needs, adjustments might be necessary
# for the script, AWS CLI configuration, or IAM permissions.

# if __name__ == '__main__':
#     # Call the get_secret function and store the result.
#     secret = get_secret()
#
#     # Print the secret value.
#     print(f"Secret: {secret}")
