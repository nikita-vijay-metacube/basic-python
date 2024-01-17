def listComment():
    """\n***Through List***\n"""
def setComment():
    """\n***Using Set***\n"""
    
print (listComment.__doc__)


countries = ['India','Nepal','Russia']
print(f"Contry list before addding the new country:{countries}")

# Append new country at the end of list
countries.append('England')
print(f"After add:{countries}")

# Remove any country using index
del countries[2]
print(f"After Removing 2nd indexed country:{countries}")

# Add new country is the middle of list
mid = len(countries)
print('Length',len(countries))
print('Mid',mid)
countries.insert(mid,'USA')
print(f"After insert into middle:{countries}")

##Using Set
print (setComment.__doc__)


countriesSet = {'India','Nepal','Russia','Japan'}
print('Country Set:',countriesSet)

# Add a new coutnry at the end or set
countriesSet.add('England')
print('Country Set after adding new Ccountry:',countriesSet)

# Remove any country from set
countriesSet.remove('Russia')
print('Country Set after removing Country:',countriesSet)

# Add a new country in the middle of set
middle_index = len(countriesSet) // 2
new_country = {'Dubai'}
print("middle_index-", middle_index)
first_half = list(countriesSet)[:middle_index]
second_half = list(countriesSet)[middle_index:]
new_set = set(first_half + list(new_country) + second_half)

print(new_set)
