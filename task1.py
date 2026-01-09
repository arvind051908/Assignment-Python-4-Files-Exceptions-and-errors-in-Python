# Task 1: Read a File and Handle Errors
import os
file_name = 'sample.txt'
if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
else:
    print(f"Error: The File '{file_name}' was not found.")







 
    

 