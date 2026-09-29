# 1. List
age = 25
has_license = False

my_list = ["Alice", 25, age, True, has_license]

my_list

name = my_list[0]
age = my_list[1]

has_license = my_list[-1] #last index

has_license

my_list[-2]

my_list[0] = "Dave"

my_list.append("Alice")

my_list.remove("Alice")

my_list.insert(1,'Alice')

my_list

# list methods

len(my_list)
my_list.count(25)
my_list.index("Alice")

num = [2,4,6,1,3,5]

num.sort()

num

num.reverse()

new_list = my_list.copy()

new_list

#2. Dictionaries

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "new york"
}

my_dict

my_dict["name"]

my_dict["name"] = "Dave"

my_dict["license"] = False

del my_dict["license"]

#3 Tuples : immutable

empty = ()
empty

point = (3,5)
point

colors = ("red", "green", "blue")

colors[0]

colors[0] = "pink" # error

# 4 : sets

empty_set = set()

numbers = {1,2,3,4,4}

numbers



