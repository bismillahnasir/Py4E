fname = "mbox-short.txt"

count = 0

with open(fname) as fh:
    for line in fh:
        if not line.startswith("From"):
            continue
        line = line.rstrip()
        words = line.split()
        if words[0] == "From:":
            continue
        print(words[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
