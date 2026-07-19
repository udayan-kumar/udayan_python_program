# PYTHON WRITING FILES (.txt , .json , .csv)
import json
import csv

# txt_data = "i love udayan"
# employees = ["udayan" , "kumar" , "mannu"]

# employee = {
#     "name" : "udayan",
#     "age" : 19,
#     "job" : "student"
# }

employee = [["name" , "age" , "job"],
            ["udayan" , 19 , "student"],
            ["kumar" , 20 , "software engeneer"],
            ["mannu" , 23 , "developer"]]

file_path = "output_txt"
file_path = "output_json"
file_path = "output_csv"

try:
    with open(file_path , "w" , newline="") as file:
        # file.write("\n" + txt_data)

        # for employee in employees:
        #     file.write(employee + "\n")

        # json.dump(employee , file , indent=4)
        # print(f"json file '{file_path}' was created")

        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")

        # print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("file already exists")