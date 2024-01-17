# x = "5"; y = "10"
# print('The value of x is {} and y is {}'.format(x,y))
# print("The value of x is "+x+" and y is "+ y)
y= input("input a number:")
x = int(y)
# print(type(x))
i=2
flag = False
while(i<x):
    if (x%i == 0):
        print(y + " is non prime number")
        flag = True
        break
    i+=1
if (flag == False):
    print(y + " is a prime number")
