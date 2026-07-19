import os

file_path = "file_detection/test.txt"

if os.path.exists(file_path):
    print(f"the location '{file_path}' exists")
else:
    print("that location doesn't exists")
