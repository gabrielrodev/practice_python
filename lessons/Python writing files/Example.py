import json
import csv
employees = {"name": "Spongebob",
             "age": 30,
             "job": "cook",}

file_path = "C:\\Users\\gabohappy\\Desktop\\output.json"


try:
    with open(file=file_path, mode="w",) as file: # w write, x write if the file does not exist, a append file, r read
        json.dump(employees, file, indent=4)                         # is like we are doing File = file
        #writer = csv.writer(file)
        #for row in employees:
        #    writer.writerow(row)
        print(f"json file '{file_path}' created!")
except FileExistsError:
    print(f"File already exists!")