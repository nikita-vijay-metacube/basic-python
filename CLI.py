import sys

n = len(sys.argv)

print("Length of arguments passed:",n)

print("\nName of python script:",sys.argv[0])

print("\nArguments passed:",end=" ")
for i in range(1, n):
    print(sys.argv[i],end=" ")

sum = 0
for i in range(1,n):
    sum+=int(sys.argv[i])
print("\nSum of all passed arguments:",sum)