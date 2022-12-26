import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments

# /home/etl/Desktop/pythonProject/HelloFriend/customer_cr/data.csv

def make_json(csvFilePath, jsonFilePath):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            key = rows['docname']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'20221226_062827.csv'
jsonFilePath = r'data.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
