# pattern 1 : importing the whole module

import math

math.sqrt(25)

#pattern 2 : importing specific item from module

from math import sqrt,pi


import random 
number = random.randint(1,10)
choice = random.choice(["apple","mango","banana","strwaberry"])

number
choice

import datetime
today = datetime.date.today()
print(today)

import os
current_dir = os.getcwd()
print(current_dir)

import json
data = {"name":"Alice", "age":30}
json_string = json.dumps(data)
print(json_string)

