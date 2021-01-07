name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
take = False
counts = dict()


for line in handle:
    for item in line.split():
        if item == "From":
            word = line.split()[-2].split(':')[0]
            counts[word] = counts.get(word, 0) + 1

#for k, v in (counts.items()): print(k, v)
for key in sorted(counts):
	print (key, counts[key])
