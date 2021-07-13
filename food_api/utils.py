import os
import boto3

def get_hostname():
    return os.uname()[1]

def get_ddb_table(table_name, table_region='us-west-1'):
    dynamodb = boto3.resource('dynamodb', region_name=table_region)
    return dynamodb.Table(table_name)