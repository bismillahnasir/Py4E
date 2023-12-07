import re
numSum = 0

fname = input("Enter file:")
if len(fname) < 1:
    fname = "regex_sum_1868206.txt"
with open(fname) as fh:

    # just checking
    mystring = (fh.read())
    print(mystring[:25])

    # Reset the cursor to the beginning of the file, otherwise fh.read will not work again
    # as the file read pointer has reached the end of the file and needs to be brought to
    # the beginning of the file again.
    fh.seek(0)

    numSum = sum([int(x) for x in re.findall('[0-9]+', fh.read())])  # List Comprehension

    print(numSum)
