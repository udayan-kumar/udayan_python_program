# PYTHON READING FILE (.txt , .json , .csv)
import json
import csv

# file_path = "D:/udayan_python_program/writing_file/output_txt"

# file_path = "D:/udayan_python_program/writing_file/output_json"

file_path = "D:/udayan_python_program/writing_file/output_csv"

try:
    with open(file_path , "r") as file:
        # content = file.read()
        # print(content)

        # content = json.load(file)
        # print(content)

        content = csv.reader(file)
        for line in content:
            print(line)
       
except FileNotFoundError:
    print("file doesn't found")
   