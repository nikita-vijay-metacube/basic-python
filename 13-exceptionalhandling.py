
class ValueInvalidPasswordExceptionError(Exception):
    """\n\n *** Invalid password Exception class called!! ***\n\n"""
    pass

try:
    inputPassword = str(input("Enter a password(8 characters or long): "))
    if len(inputPassword) < 8:
        raise ValueInvalidPasswordExceptionError
    else:
        print("You entered valid password: ", inputPassword)
except ValueInvalidPasswordExceptionError:
        print (ValueInvalidPasswordExceptionError.__doc__)
        print("Please Enter password having length equal to or more than 8!")

    

