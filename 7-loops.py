
y= input("input a number less than 100:")
x = int(y)
# print(type(x))
i=1
if(x >= 100):
    print("Please Enter Number less than 100")
else:
    while(i<x):
        if (i%10 != 0):
            print(i)
            print(" ")
        i+=1
