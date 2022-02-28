large = None
small = None

while True:
    num = input("enter a number: ")
    if num == "done" : 
        break
    try:
        num = int(num)
        if large is None or large < num : 
            large = num
        if small is None or small > num : 
            small = num
    except ValueError:
        print ("Invalid input")
        continue
    
print ("Maximum is", large)
print ("Minimum is", small)