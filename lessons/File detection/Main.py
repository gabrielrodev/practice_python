# Python file detection
# Relative = folder/test.txt
# Absolute = C:/Users/BroCode/Desktop/test.txt



import os  # os means operating system

file_path = "C:/Users/gabohappy/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists!")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist!")