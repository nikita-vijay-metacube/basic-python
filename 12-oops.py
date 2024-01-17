from abc import ABC, abstractmethod

"""Encapsulation Assignment"""

class Patient: 
    def __init__(self):
        self.id = 0
        self.name =''
        self.ssn =0

    def setData(self, id, name, ssn):
        self.id = id
        self.name = name
        self.ssn = ssn

    def getData(self):
        return {'id':str(self.id), 'name':self.name, 'ssn':str(self.ssn)}

firstPatient = Patient()
firstPatient.setData(1,'Rakesh', 1)
secondPatient = Patient()
secondPatient.setData(2,'lokesh', 2)
firstList = firstPatient.getData()
secondList = secondPatient.getData()
print("Patient",firstList['id'],  "| Name:",  firstList['name'],  " ssn:",  firstList['ssn'])
print("Patient",secondList['id'],  "| Name:",  secondList['name'],  " ssn:",  secondList['ssn'])


print("""Abstract Class Assignment""")


class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        print("1134")
        pass
# a = TouchScreenLaptop()

class hp(TouchScreenLaptop):
    def scroll(self):
        pass

class dell(TouchScreenLaptop):
    def scroll(self):
        pass

class hpnotebook(hp):
    def click(self):
        print("34")
        super().click()
        pass
        
class dellnotebook(dell):
    def click(self):
        print("15")

hpnotebookObj = hpnotebook()
hpnotebookObj.click()


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
