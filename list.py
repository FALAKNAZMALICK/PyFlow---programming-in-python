# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
list:
    COLLECTION OF DATA STORED UNDER ONE VARIABLE
    IT CAN BE OF ANY DATA TYPE
    IT CAN BE CHANGEABLE/EDITABLE
    IT CAN BE DISPLAYED
    SQUARE BRACKETS ARE USED TO INITIALIZE LIST []
    THE DATA TYPE INSIDE LIST CAN BE INCONSISTENT
"""


l1=[1,2,3,4.1,5,6,7,8,9,True]
print(l1)

#length
length= len(l1)
print(length)

#upddate
l1[1] = 'a'
print(l1)

#append
l1.append('new element')
print(l1)

#SYNTAX FOR THE SERIES OF ELEMENTS / MINI LIST->
#LISTNAME[STARTFROM : ENDBEFORE]
print(l1[2:3])

#insert
l1.insert(5, False)
print(l1)

#EXTEND
l2=['falak', 1.0]
l1.extend(l2)
print(l1)
#REMOVE->ELEMENT
#POP->INDEX
l1.remove(False)
l1.pop(4)
print(l1)

#del->TO DELETE WHOLE LIST
#clear->TO DELETE LIST CONTENT
#SORT
l1.sort()
print(l1)

