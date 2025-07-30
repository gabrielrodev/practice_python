#Python writing files (.txt, .json, .csv)

txt_data = "I like chalupa"

file_path = "C:\\Users\\gabohappy\\Desktop\\output.txt"


try:
    with open(file=file_path, mode="a") as file: # w write, x write if the file does not exist, a append file, r read
        file.write("\n" + txt_data)                                     # is like we are doing File = file
        print(f"txt file '{file_path}' created!")
except FileExistsError:
    print(f"File already exists!")