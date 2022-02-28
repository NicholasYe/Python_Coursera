number = input("number:")
number = float(number)

if (number>0.0 and number<1.0):
    number = number
else: 
    number = -1

if number >= 0.9:
    print ("A")
elif number >= 0.8:
    print ("B")
elif number >= 0.7:
    print ("C")
elif number >= 0.6:
    print ("D")
elif number < 0.6:
    print ("F")
else:
    print ("Error!")
