import re

hoursCounts = dict()

fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
with open(fname) as fh:
    for line in fh:
        # if line.find("From ") == -1:
        #    continue
        if not re.search("^From ", line):
            continue
        # print(line)
        words = line.split()
        hours = words[5].split(":")[0]
        hoursCounts[hours] = hoursCounts.get(hours, 0) + 1


for hours, count in sorted(hoursCounts.items()):
    print(hours, count)
