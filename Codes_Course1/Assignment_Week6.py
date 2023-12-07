def computepay(hours, rate_per_hour):

    if h > 40:
        return 40 * r + 1.5 * (h - 40) * r
    else:
        return h * r


hrs = input("Enter hours: ")
rph = input("Enter rate per hour: ")

h = float(hrs)
r = float(rph)

p = computepay(h, r)
print("Pay", p)