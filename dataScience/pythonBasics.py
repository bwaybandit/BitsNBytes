# Slices
a = '12345'
print("SLICE (first 3) : {}".format(a[0:3]))   # will return 123
print("SLICE (start at 1 and include everything except last)s : {}".format(a[1:-1]))  # will return 234

# Lists (can take any data type)
a = [1,2,3]
b = ['f', 'g', 'h', ['1','2','3']]
a.append('S')
print("LIST : [1,2,3] : {}".format(a))                                 # will return 1,2,3,'S'
print("LIST : ['f','g','h',['1','2','3']] : {}".format(b[3][2]))       # will return 3

# Dictionaries
a = {'key1':'value1', 'key2':'value2'}
print("Dictionary (key/value) : {}".format(a['key1']))   # will return 'value1'

# Tuples
a = (1,2,3)
print("TUPLE (a,b,c) : {}".format(a[1]))    # will return 2

# Tuples are immutable (cells cannot be reassigned)

# Sets - collection of unique elements
a = {1,2,3}
a.add(5)
print("SET - unique collection of elements : {}".format(a))   # will return [1,2,3,5]

# if-elif-else
if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle in IF-ELIF-ELSE')
else:
    print('last')

# for loop
a = [1,2,3,4,5]
for ctr in a:
    print("ctr in FOR loop is :{}".format(ctr))

# while loop
i = 1
while i < 5:
    print("i in WHILE loop is:{}".format(i))
    i = i + 1

# range
for i in range(4):
    print("Range (generator) : {}".format(i))

# list comprehension
x = [1,2,3,4]
print("List Comprehension : {[item ** 2 for item in x]}")

# Functions
def myFunc(x=2):
    """
    Doc String
    """
    return x*x
print("Function myFunc() returns : {}".format(myFunc()))
print("Function myFunc() returns : {}".format(myFunc(3)))

# Map function
seq = [1,2,3,4,5]
print("MAP function: {}".format(list(map(myFunc, seq))))

# Lambda Expression
print("Lambda Expression : {}".format(list(map(lambda num: num*num,seq))))

# Filter out members of a sequence
print("FILTER: {}".format(list(filter(lambda num:num%2 == 0,seq))))