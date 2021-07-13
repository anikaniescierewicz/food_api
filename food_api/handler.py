import json
from os import environ
from food_api.utils import get_hostname, get_ddb_table 

def hello(event, _context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "hostname": get_hostname()
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def get_categories(_event, _context):
    table_name = f"{environ['STAGE']}-food"
    table = get_ddb_table(table_name)
    categories = table.get_item(Key={'PK': 'CATEGORIES', 'SK': 'CATEGORIES'})
    cat_list = list(categories["Item"]["category_list"])
    return cat_list
    # body = {
    #    "categories": categories
    # }

    # response = {
    #     "statusCode": 200,
    #     # the same as JSON.stringify
    #     "body": json.dumps(body)
    # }
    # return response
