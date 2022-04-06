name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lst = list()
for line in handle:
    if not line.startswith("From:"): 
        continue
    line = line.split()
    lst.append(line[1])

dic = dict()
for word in lst:
    dic[word] = dic.get(word, 0) + 1

bigkey = None
bigvalue = None

for key,value in dic.items():
    if bigvalue is None or value > bigvalue:
        bigkey = key
        bigvalue = value

print(bigkey, bigvalue)