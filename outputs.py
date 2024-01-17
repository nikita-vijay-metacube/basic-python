print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='**')
print(1, 2, 3, 4, sep='#', end='\n')
# format() with variables
x=5
y=6
print("Value of x : {} and y : {}".format(x,y),end='\n')
print("I love {0}. I is easy to {1}".format('Pyhton','learn'))
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
num = 2.14
print('Num:%1.2f'%num)
assert(1==1),'not solved'