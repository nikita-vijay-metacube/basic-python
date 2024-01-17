my_list = ['p', 'r', 'o', 'b', 'e']
n_list = ["Happy", [2, 0, 1, 5]]
print(n_list[1][3])
odd = [1, 9, 2,6,4,9,0,12,45,34,23,56]
odd.insert(1,3)

print(odd)
odd[2:2] = [5, 7]
print(odd)

# Generate list for store countries
countries = ['Nepal','Bhutan','China']
print(f"Before add:{countries}")

# Append new country at the end of list
countries.append('India')
print(f"After add:{countries}")

# Remove any country using index
del countries[2]
print(f"After add:{countries}")

# Add new country is the middle of list
mid = len(countries) //2
print('Length',len(countries))
print('Mid',mid)
countries.insert(mid,'USA')
print(f"After insert into middle:{countries}")




##
countriesSet = {'Nepal','Bhutan','China','Venice'}
print('Country Set:',countriesSet)

# Add a new coutnry at the end or set
countriesSet.add('India')
print('Country Set After Adding New Country:',countriesSet)

# Remove any country from set
countriesSet.remove('Nepal')
print('Country Set After Removing Country:',countriesSet)

# Add a new country in the middle of set
middle_index = len(countriesSet) // 2
new_country = {'Shri Lanka'}
first_half = list(countriesSet)[:middle_index]
second_half = list(countriesSet)[middle_index:]
new_set = set(first_half + list(new_country) + second_half)

print(new_set)
