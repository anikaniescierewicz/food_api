import json
from food_api.utils import get_hostname

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
