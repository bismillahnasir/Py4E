# Use words.txt as the file name
fname = input("Enter file name: ")


with open(fname) as fh:
    inp = fh.read()
    inp = inp.rstrip()
    print(inp.upper())

