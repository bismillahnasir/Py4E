largest = None
smallest = None
while True:
    num = input("Enter an integer number: ")
    if num == "done":
        break
    try:
        num_int_current = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = num_int_current
        smallest = num_int_current
    elif num_int_current > largest:
        largest = num_int_current
    elif num_int_current < smallest:
        smallest = num_int_current

print("Maximum is", largest)
print("Minimum is", smallest)
