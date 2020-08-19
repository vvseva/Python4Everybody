# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
val = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    line = line.replace('X-DSPAM-Confidence:', '')
    line = float(line)
    val = val+line
print('Average spam confidence:',val/count)
#print("Done")
