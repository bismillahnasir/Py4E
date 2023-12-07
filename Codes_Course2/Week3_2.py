# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
with open(fname) as fh:
    count = 0
    val = 0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        ind = line.find(':')
        val_str = (line[ind+1:]).strip()
        val_flt = float(val_str)
        val = val + val_flt
        # print(val_flt)
        # print(val)
        count = count + 1

avgSpamConf = val / count
print("Average spam confidence:", avgSpamConf)
