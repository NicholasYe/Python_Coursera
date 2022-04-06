counts = dict()
names = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'aaa', 'ccc']
for test in names:
    counts[test] = counts.get(test, 0) + 1
print(counts)