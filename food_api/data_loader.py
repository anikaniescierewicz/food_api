"""
Script for loading data into DynamoDB
"""
# importing modules
import csv
import time
from botocore.exceptions import ClientError
from food_api.utils import get_ddb_table

# csv file name
FILENAME = "data/food.csv"
TABLE_NAME = 'dev-food'

def load_data_from_csv() -> tuple:
    """
    Load CSV file and returns an array of headers and an array of rows
    """
    # initializing the titles and rows list
    rows = []
    # reading csv file
    with open(FILENAME, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting field names through first row
        fields = next(csvreader)
        # extracting each data row one by one
        for row in csvreader:
            #drop items that have a space in the category name (we want only basic foods)
            if not ' ' in row[0]:
            # if not row[0] == 'No Category':
                rows.append(row)
    #  printing first 5 rows
    print('\nFirst 5 rows are:\n')
    for row in rows[:5]:
        # parsing each column of a row
        for idx, col in enumerate(row):
            print(f"{fields[idx]}: {col}")
        print('\n')
    return (fields, rows)

def get_categories(rows: list) -> set:
    """
    Get a list of unique categories from all rows
    """
    return set([x[0] for x in rows]) # pylint: disable=consider-using-set-comprehension

def add_categories(table, categories: set) -> None:
    """
    Add Categories item to DynamoDB
    """
    table.put_item(
        Item={
            'PK': 'CATEGORIES',
            'SK': 'CATEGORIES',
            'category_list': categories
        }
    )

def build_dynamodb_item_dict(item: list, headers: list) -> dict:
    """
    Build a dictionary from the item list to be sent to DynamoDB
    """
    # Create dict with header and corresponding item
    # because we will be adding Item to dynamodb
    # which has to be of type dict
    item_dict = {header:item[idx] for idx, header in enumerate(headers)}
    # Adding SK and PK for each item
    item_dict['SK'] = item_dict['Nutrient Data Bank Number']
    item_dict['PK'] = item_dict['Category']
    return item_dict

def add_items(table, items: list, headers: list) -> None:
    """
    Add all passed items to the DynamoDB table
    """
    # table.batch_writer allows you to write multiple items at once
    with table.batch_writer() as batch:
        # Looping through items array
        for item in items:
            try:
                # Create dict with header and corresponding item
                # because we will be adding Item to dynamodb
                # which has to be of type dict
                item_dict = build_dynamodb_item_dict(item, headers)
                print(f'adding item {item_dict["Description"]}')
                # Adding each item to dynamodb
                batch.put_item(Item=item_dict)
            except ClientError as err:
                if err.response['Error']['Code'] == "ProvisionedThroughputExceededException":
                    print('throttled, sleeping')
                    # wait 30 seconds
                    time.sleep(30)
                    # try adding item again
                    batch.put_item(Item=item_dict)
                else:
                    raise err


def load_data() -> None:
    """
    Main data loader function
    """
    csv_fields, csv_rows = load_data_from_csv()
    # get total number of rows
    print(f"Total no. of rows: {len(csv_rows)}")
    # printing the field names
    print('Field names are: ' + ', '.join(csv_fields))
    categories = get_categories(csv_rows)
    print(f'Identified {len(categories)} categories')
    table = get_ddb_table(TABLE_NAME)
    add_categories(table, categories)
    add_items(table, csv_rows, csv_fields)

if __name__ == "__main__":
    load_data()
