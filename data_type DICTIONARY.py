# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"""
DICTIONARY: 
    collection of data stored under one variable
    it can be of any data type
    curly brackets are used to initialize set {}
    DICT MUST HAVE A KEY VALUE PAIR
    it can be displayed
    the data type inside a dict can be inconsistent
    no duplication is allowed
    it is changeable , editable, ordered(>=3.7 version), accessible
    for a key, multiple values is allowed in the form of list, set, tuple or dict.
    
    
    USE: for mapping purpose
    
    
    initialization
    print
    length
    accessibility through key instead of indexes OR using method .get() 
    .keys()
    .values()
    .update()
    add/remove an item
    
    dict inside a dict = nested dict

"""


d1 = {
  "brand": { "name" : "Ford"},
  "model": "Mustang",
  "year": 1964,
  "year": 1960
}

print(d1)

print(d1["brand"])
print(d1.get("model"))


d1.keys() ##to print the keys in a dict

d1.values() ##to print the values in a dict

d1.items() ##to print the key,value pair in a dict

##to change the value of an item
d1["model"] = 'abc'
print(d1)
d1.update({"year": 2020})

## add an item (key/value pair)
d1["color"] = "red"
print(d1)


#d1.pop("brand") ## removes key brand
#d1.popitem() ## removes last inserted item





