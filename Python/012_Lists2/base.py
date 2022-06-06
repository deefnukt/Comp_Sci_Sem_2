import random
thislist = [0,1,2,3,4,5,6,7,8,9,10,11]
x= int (input("How many numbers would you like to print(1-10)?"))
for i in range (x):
    print(thislist[random.randrange(0,10)])

