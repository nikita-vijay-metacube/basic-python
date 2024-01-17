
A test case for quiz resolution
class Human:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()
    
    class Head:
        def talk(self):
        	return 'talking...'

    # guido = Human()
guidoh = Human().head
#  print (guido.name)
print (guidoh.talk())