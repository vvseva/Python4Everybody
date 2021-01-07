name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
take = False
counts = dict()

for line in handle:
    for word in line.split():
        if take:
            counts[word] = counts.get(word, 0) + 1
            take = False
            
        if word == "From":
            take = True
            pass
        
mostcommiter = None
mostcounts = 0
for mail, count in counts.items():
    if count >= mostcounts:
        mostcounts = count
        mostcommiter = mail
print(mostcommiter, mostcounts)
            
