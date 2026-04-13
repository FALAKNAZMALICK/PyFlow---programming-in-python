# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 14:13:54 2026

@author: usama.khan
"""

"""
LIST: 
    collection of data stored under one variable
    it can be of any data type
    it is changeable/editable
    it can be displayed
    square brackets are used to initialize list []
    the data type inside a list can be inconsistent
    
    
    initialization
    access/print
    length
    update
    append
    slicing


"""

l1 = [1,2,3,4,5,6,7,8,9]
l2 = l1.copy()
print(l1)

## length of the list
length_of_l1 = len(l1)
print(length_of_l1)

 

#append an element
l1.append('new element')
print(l1)

'''
#i have a list of length 50 , i want to check 31-40 element.
# SYNTAX for the series of elements/ mini list -> list_name[start_from_index:end_before_index:gap]
# next = start +gap = 0+1 + 1 = l1[1]


for(i=0;i<=12;i+=2)
{
 cout(l1[i]);
 }

1
'a'
2
3
4.1
.
.
new element

'''