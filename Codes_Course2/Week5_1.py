emailCounts = dict()

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
        emailCounts[words[1]] = emailCounts.get(words[1], 0) + 1

bigEmail = None
bigCount = None

for email, count in emailCounts.items():
    if bigCount is None or count > bigCount:
        bigEmail = email
        bigCount = count

print(bigEmail, bigCount)
