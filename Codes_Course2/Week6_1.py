hoursCounts = dict()

fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
with open(fname) as fh:
    for line in fh:
        if not line.startswith("From"):
            continue
        # line = line.rstrip()
        words = line.split()
        if words[0] == "From:":
            continue
        hours = words[5].split(":")[0]
        hoursCounts[hours] = hoursCounts.get(hours, 0) + 1


for hours, count in sorted(hoursCounts.items()):
    print(hours, count)
