"""
Lambda handler functions
"""
from os import environ
from boto3.dynamodb.conditions import Key
from food_api.utils import get_ddb_table, lambda_response

def get_categories(_event: dict, _context: dict) -> dict:
    """
    Query DynamoDB and return list of categories
    """
    table_name = f"{environ['STAGE']}-food"
    table = get_ddb_table(table_name)
    categories = table.get_item(Key={'PK': 'CATEGORIES', 'SK': 'CATEGORIES'})
    cat_list = list(categories["Item"]["category_list"])
    body = {
       "categories": cat_list
    }

    return lambda_response(body)

def get_food_category(event: dict, _context: dict) -> dict:
    """
    Query list of food in a given category
    """
    table = get_ddb_table(f"{environ['STAGE']}-food")
    category = event["pathParameters"]["category"]
    ddb_response = table.query(
        KeyConditionExpression=Key('PK').eq(category)
    )
    items = [{'food_id': x['SK'], 'description': x['Description']} for x in ddb_response['Items']]
    body = {
       "category": category,
       "items": items,
       "count": ddb_response['Count']
    }
    return lambda_response(body)

def get_single_food(event: dict, _context: dict) -> dict:
    """
    Get single food within given category
    """
    table = get_ddb_table(f"{environ['STAGE']}-food")
    category = event["pathParameters"]["category"]
    food_id = event["pathParameters"]["food_id"]
    ddb_response = table.get_item(
        Key={'PK': category, 'SK': food_id}
    )
    item = ddb_response.get("Item")
    if item:
        body = {
            "item": item
        }
        status_code = 200
    else:
        body = "Item not found"
        status_code = 404
    return lambda_response(body, status_code)
