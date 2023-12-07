import re
numSum = 0

fname = input("Enter file:")
if len(fname) < 1:
    fname = "regex_sum_1868206.txt"
with open(fname) as fh:
    for line in fh:
        numListSTR = re.findall('[0-9]+', line)
        if len(numListSTR) == 0:
            continue
        # print(numListSTR)
        numSum = sum([int(x) for x in numListSTR]) + numSum

    print(numSum)
