
with open ('text.txt', 'r', encoding='utf-8') as f:
    data_log = []
    line = f.readline()
    while line:
        data = line.split()
        data_log.append((data[0], data[5],data[6]))
        line = f.readline()
print(data_log)