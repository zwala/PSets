#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:25:39 2019

@author: zwalaneelam
"""

#Newton-Raphson
epsilon=0.01
y=54.0
guess=y/2.0
numOfGuesses=0

while abs(guess**2 - y)>=epsilon:
    numOfGuesses+=1
    guess= guess- (((guess**2)-y)/(2*guess))
print ('numOfGuesses:' +str(numOfGuesses))
print('Squareroot of'+str(y)+ 'is about:'+str(guess))

def a(x):
    return x+1

print (a(2))
print (a(2.0))