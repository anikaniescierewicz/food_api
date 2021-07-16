"""
Helper/util functions
"""
import os
import json
import boto3

def get_hostname():
    """
    Returns hostname of the system where the code is being executed
    """
    return os.uname()[1]

def get_ddb_table(table_name, table_region='us-west-1'):
    """
    Given a DynamoDB table name, returns the Boto3 DynamoDB Table resource
    """
    dynamodb = boto3.resource('dynamodb', region_name=table_region)
    return dynamodb.Table(table_name)

def lambda_response(body: any, status_code: int = 200) -> dict:
    """
    Returns API Gateway compatible Lambda response
    """
    return {
        "statusCode": status_code,
        # the same as JSON.stringify
        "body": json.dumps(body)
    }
