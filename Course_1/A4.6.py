def computepay(h,r):
    if h > 40:
        return (40*r) + (h-40) * (r*1.5)
    else:
        return h * r

hrs = input("hours:")
rate = input("rate:")

hrs = float(hrs)
rate = float(rate)

p = computepay(hrs, rate)
print("Pay",p)