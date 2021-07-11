# importing csv module
import csv

# csv file name
filename = "data/food.csv"

def load_data_from_csv():
    # initializing the titles and rows list
    rows = []
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting field names through first row
        fields = next(csvreader)
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    #  printing first 5 rows
    print('\nFirst 5 rows are:\n')
    for row in rows[:5]:
        # parsing each column of a row
        for idx, col in enumerate(row):
            print(f"{fields[idx]}: {col}"),
        print('\n')
    return (fields, rows)

def get_categories(rows):
    # categ = []
    # for row in rows:
    #     categ.append(row[0])
    return set([x[0] for x in rows])

def load_data():
    csv_fields, csv_rows = load_data_from_csv()
    # get total number of rows
    print(f"Total no. of rows: {len(csv_rows)}")
    # printing the field names
    print('Field names are: ' + ', '.join(csv_fields))
    categories = get_categories(csv_rows)
    print(f'Identified {len(categories)} categories')

if __name__ == "__main__":
    load_data()