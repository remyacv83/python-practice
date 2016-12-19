import os
from string import digits
def rename_files():
    #(1) get file name from a folder
    file_list = os.listdir(r"C:\python_code\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\python_code\prank")
    #(2) for each file in prank folder, rename filename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path) 

rename_files()
