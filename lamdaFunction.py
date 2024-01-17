from functools import reduce

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda x:x%2==0,nums))
print('all evens from list:',evens)

doubals = list(map(lambda x: x*2, evens))
print("Doubals of all elements:",doubals)

sum = reduce(lambda a,b:a+b, doubals)
print("Sum of all doubals list:",sum)