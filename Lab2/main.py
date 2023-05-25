f = open("./hosts2.txt","r")

hosts_data = []
for line in f.readlines():
    if line[0] == '#':
        continue
    try:
        hosts_data.append(line.split()[1])
    except IndexError: continue

f.close()

f = open("./dns.log","r")

logs_data = []

for line in f.readlines():
    if (line[0] == '#'):
        continue
    logs_data.append(line.split()[9])

f.close()

cnt = 0
for i in range(len(logs_data)):
    if logs_data[i] in hosts_data:
        cnt += 1

print("Количество совпадений -",cnt)