import os
from shutil import copy

def create_file (path, dir_name, file_name):
    file_path = os.path.join(path, "templates", dir_name)
    if not os.path.isdir(file_path):
        copy(file_path,file_path)
    file = os.path.join(file_path, file_name)
    with open(file, 'w') as f:
        print(f'{file} created')

path = 'C:\\Users\\Ольга\\Documents\\GeekBrains\\PyProjects\\guseva_olga_dz\\Guseva_Olga_dz_7\\my_project'
for root, dirs, files in os.walk(path):
    for file in files:
        if file.split('.') == 'html':
            folder_name = os.path.split(root)[-1]
            create_file(path, folder_name, file)
