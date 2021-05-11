import os

path = 'C:\\Users\\Ольга\\Documents\\GeekBrains\\PyProjects\\guseva_olga_dz\\Guseva_Olga_dz_7\\some_data'

resilt_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0}

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    size = os.stat(file_path).st_size
    if size < 100:
        resilt_dict[100] += 1
    elif size < 1000:
        resilt_dict[1000] += 1
    elif size < 10000:
        resilt_dict[10000] += 1
    elif size < 100000:
        resilt_dict[100000] += 1

print(resilt_dict)
