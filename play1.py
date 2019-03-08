"""
Assume s is a string of lower case characters.
Write a program that prints the longest substring 
of s in which the letters occur in alphabetical order.
 For example, if s = 'azcbobobegghakl', then your 
 program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. 
We encourage you to work smart. 
If you've spent more than a few hours on this problem, 
we suggest that you move on to a different part of the 
course. If you have time, come back to this problem 
after you've had a break and cleared your head.
"""
"""
s='abc'
prevChar=''
currentString=''
longestString=''
for char in s:
    if prevChar <=char:
        currentString+=char
        if len(currentString)>len(longestString):
            longestString=currentString
    else:
        currentString=char
    prevChar=char
print (longestString)

"""
s='abcdefgakblmocpqrs'
currentChar=''
longest=''
previous=''

for each in s:
    if each>=previous:
        currentChar+=each
        if len(currentChar)>len(longest):
            longest=currentChar
    else:
        currentChar=each    
    previous=each
print (longest)






























#print ("Longest substring in alphabetical order is:",longString)