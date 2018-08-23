import os
import re

def rename_files():
  file_list = os.listdir(r"E:\Nauka\python\udacity\Programming Foundations with Python\photos")
  saved_path = os.getcwd()

  os.chdir(r"E:\Nauka\python\udacity\Programming Foundations with Python\photos")
  for file_name in file_list:
    os.rename(file_name, re.sub('[0-9]', '', file_name))

  os.chdir(saved_path)

if __name__ == "__main__":
  #print(os.getcwd())
  rename_files()