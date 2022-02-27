hrs = input("hours:")
rate = input("rate:")

if float(hrs) <= 40:
    pay = float(hrs) * float(rate)
elif float(hrs) > 40:
    pay = 40*float(rate) + (float(hrs)-40)*float(rate)*1.5

print(pay)