import re

hoursCounts = dict()
count = 0
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
with open(fname) as fh:
    for line in fh:
        if not re.search("From ", line):
            continue
        # print(re.findall("@(\S+)", line))
        hostID = re.findall("^From .*@([^ ]*)", line)
        if hostID is not []:
            print(hostID)
            count = count + 1

    print(count)
