x = int (input("please enter a number"))
y = input("please enter an operation")
z = int (input("please enter another number"))

if (y == "+"):
    print (x+z)
elif (y == "-"):
    print (x-z)
elif (y == "/"):
    print (x/z)
elif (y == "*"):
    print (x*z)
else:
    print ("Please enter a valid operation")
