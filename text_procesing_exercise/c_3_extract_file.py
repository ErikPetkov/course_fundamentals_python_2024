file_path = input().split("\\")
file_date = file_path[-1]
file_name,file_extention = file_date.split(".")
print(f"File name: {file_name}")
print(f"File extension: {file_extention}")