print "Type List"
"""
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type. 

If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. 

At the end of your program print the string, the number and an analysis of what the list contains. 

If it contains only one type, print that type, otherwise, print 'mixed'.

"""

def type(list):
    st=""
    sum=0

    for element in list:
        if isinstance(element, int) or isinstance(element, float):
            sum+= element
        elif isinstance(element, str):
            st+= element+ " "

    if len(st)>0 and sum>0:
        print "The list you entered is of mixed type"
        print "Sum:",sum
        print "String:", st
    elif len(st)>0:
        print "The list you entered is of string type"
        print "String:", st
    else:
        print "The list you entered is of integer type"
        print "Sum:", sum
            
#input
list1 = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# input
list2 = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"

# input
list3 = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"

print "List1"
type(list1)

print "List2"
type(list2)

print "List3"
type(list3)