#!/usr/bin/env python3
import os

file_name = 'temp.csv'

full_path = __file__
print(f'The full file path is: "{full_path}"')

dir_name = os.path.dirname(full_path)
print(f'The full path directory is: {dir_name}')

file_path = os.path.join(dir_name, file_name)
print(f'The file path is: {file_path}')
