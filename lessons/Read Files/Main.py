# Python reading files (.txt, .json, .csv)
import json
import csv


""" ____________________TXT FILE____________________
file_path = "C:/Users/gabohappy/Desktop/output.txt"

try: 
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file not found")
except PermissionError:
    print("You don't have permission to read file")
"""
""" ____________________JSON FILE____________________
file_path = "C:/Users/gabohappy/Desktop/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["name"])
except FileNotFoundError:
    print("That file not found")
except PermissionError:
    print("You don't have permission to read file")
"""
file_path = "C:/Users/gabohappy/Desktop/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for row in content:
            print(row[2])   #You can do an index to get a specified colum
except FileNotFoundError:
    print("That file not found")
except PermissionError:
    print("You don't have permission to read file")