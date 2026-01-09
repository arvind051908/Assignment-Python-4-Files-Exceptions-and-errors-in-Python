# Task 2: Write and Append Data to a File
user = input("Enter text to write to the file: ")
file = open("output.txt", "w")
file.write(user + "\n")
file.close()
print("Data successfully written to output.txt.\n")

user = input("Enter additional text to append: ")
file = open("output.txt", "a")
file.write(user + "\n")
file.close()
print("Data successfully appended.\n")

print("Final contents of output.txt:")

file = open("output.txt", "r")
print(file.read())
file.close()


