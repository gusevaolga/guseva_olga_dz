import os

blank = {'my_project': ['settings','mainapp', 'adminapp', 'authapp']}

for key, value in blank.items():
    if not os.path.isdir(key):
        os.mkdir(key)
    for folder_name in value:
        dir_path = os.path.join(key, folder_name)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
