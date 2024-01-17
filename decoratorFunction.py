def deco(fun):
    def inner():
        result = fun()
        return result*2
    return inner

def num():
    return 5

resultFunc = deco(num)
print("Manual call",resultFunc())

@deco
def doubals():
    return 5

print("Call by @deco:",doubals())

def addStatment(showName):
    def modify(n):
        statement = showName(n)
        statement += ", How are you?"
        return statement
    return modify

@addStatment
def showName(username):
    return "Hello "+username

print(showName("Ronak"))