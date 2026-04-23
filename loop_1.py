# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:42:46 2026

@author: usama.khan
"""

"""
LOOP: (iteration)
    
    1- For loop
    initialization, skip, end
    
    Keyword: IN --> included
    
    
    Method: Range()

"""


'''for (i=0; i<10; i++)
    { print(i);}
'''

print("For Range Method:")
for i in range(1,11,2):
    print(i)
    
print()

#############
    
l1 = [2,65,32,1]

print("For List:")
for i in l1:
    print(i)
    
print()

############

print("For alpha-numeric ")

s1 = "PYTHON"
for i in s1:
    print("Hello " , i)
    
print()

############

print("without using Zip - 2 lists ")
list_1 = [0, 1, 2]
list_2 = ["a", "b", "c"]
for i in range(3):
    print(list_1[i], list_2[i])    
    
print()

############

print("Using Zip ")

for i in zip(list_1, list_2):
    print(i)

print()

############


print("Looping a dict ")

d1 = {
  "brand": { "name" : "Ford"},
  "model": "Mustang",
  "year": 1964,
  "year": 1960
}

for key,value in d1.items():
    print("Key: ", key, " Value: ", value)
    
    
print()

#############
    
l1 = [2,65,32,1]

print("For List with enumeration (index & value):")
for i in enumerate(l1):
    print(i)
    
print()
    
    
    
    
    
