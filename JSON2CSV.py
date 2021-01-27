# This program converts JSON files to CSV, while dealing with encoding issues

import json
import csv

# Code altered from https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
# and https://stackoverflow.com/questions/21058935/python-json-loads-shows-valueerror-extra-data/51830719

temp_storage = []

# Replace the filename allrecipes-recipes.json with the json file to convert
for line in open('allrecipes-recipes.json', 'r'):
	temp_storage.append(json.loads(line)) 

# This creates the end file and deals with encoding issues; rename the file recipes.csv as desired
data_file = open('recipes.csv', 'w', encoding='utf-8')

csv_writer = csv.writer(data_file)

# This is to write the headers for the csv file
count = 0

# This goes through the JSON lines and writes them to the csv
for row in temp_storage:
	if count == 0:
		header = row.keys()
		csv_writer.writerow(header)
		count += 1

	csv_writer.writerow(row.values())

data_file.close()