# dicts in python (key-value pairs)
print('---> dicts in python')

# declaration + assignment   O(n)
print('-> declaration + assignment')

myDict = dict()
print(myDict)
myDict2 = {}
print(myDict2)

engSpn = dict(one='uno', two='dos', three='tres')
print(engSpn)
engSpn2 = {'one':'uno', 'two':'dos', 'three':'tres'}
print(engSpn2)
engSpn3_list = [('one', 'uno'), ('two', 'dos'), ('three', 'tres')]
engSpn3 = dict(engSpn3_list)
print(engSpn3)
print()

# access   O(1)
print('-> access')
print(f'key: one - value: {engSpn['one']}')
print()

# insertion/update   O(1)
print('-> insertion/update')
test = {'test1':'test1'}
test['test2'] = 'test3' # insertion
test['test1'] = 'test2' # update
print(test, '\n')

# traversal   O(n )
print('-> traversal')
def dictTraversal(dict):
    for key in dict:
        print(key, dict[key])
dictTraversal(engSpn)
print()

# search   O(n)
print(' -> search')
def searchDict(dict, value):
    for key in dict:
        if(dict[key] == value):
            return key, value
    return 'the value does not exist'
print(searchDict(engSpn, 'dos'), '\n')

# deletion   O(1)
print(' -> deletion')
del engSpn['three']
print(engSpn)
print(engSpn.pop('two', None))   # if key not found, returns None
print(engSpn.popitem())   # removes+returns last inserted element
engSpn['one'] = 'uno'
engSpn.clear()   # removes all key-value pairs from dict
print(engSpn, '\n')

# other methods
print(' -> other methods')
numbers = {'one': 1, 'two': 2, 'three':3}
numbers2 = numbers.copy()
newDict = {}.fromkeys([1,2,3], 0)
print(newDict)
print(numbers.get('one'))
print(numbers.get('four'))
print(numbers.items())
print(numbers.keys())
print(numbers.values())
numbers.setdefault('four', 4)
print(numbers)
numbers.update({'three': 0, 'five': 5})
print(numbers, '\n')
numbers['three'] = 3

# operations
print(' -> operations')
print('three' in numbers)   # checks for key
print(3 in numbers.values())   # checks for value
print(len(numbers))   # number of pair
print(all(numbers))   # checks if every value is True
print(any(numbers))   # checks if any value is True
print(sorted(numbers))   # sorts dict by key 

# dict comprehension
import random
print(' -> dict comprehension')
cities = ['paris', 'london', 'rome', 'berlin', 'madrid']
cityTemps = {city:random.randint(20,30) for city in cities}
print(cityTemps)

cityTemps25 = {city:temp for (city,temp) in cityTemps.items() if temp > 25}
print(cityTemps25)

