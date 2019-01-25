#!/usr/bin/env python2
# -*- coding: utf-8 -*-

### NUMBER SYSTEM ###
''' Number System: The process of creating numbers using some set of digits
    Types: Binary, Deciamal, Octal, HexaDecimal Number System


 Binary Number System: {0,1}
    {zeros and ones} Radix/Base: 2
    Representation: 0b... ex: 0b0110010

 Decimal Number Sytem: {0,1,2,3,4,5,6,7,8,9}
    {all single digit numbers}, Radix/Base: 10
    Representation: ... ex: 1234

 Octal Number System: {0,1,2,3,4,5,6,7}
    {0 to 7}, Radix/base: 8
    Representation:0... ex:01234

 HexaDecimal Number System: {0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}
    {0 to 9, A to F} Radix/Base: 16
    Representation: 0X... ex:0X1234
int(string,base) Converts any number to decimal
bin() Converts any number to binary
oct() Converts any number to Octal
hex() Converts decimal to HexaDecimal'''


binary=raw_input("Enter a Binary number('0b'+{0,1}): ")
decimal=raw_input("Enter a Decimal number{1 to 9}: ")
octal=raw_input("Enter a Octal number('0'+{0 to 7}): ")
hexa_decimal=raw_input("Enter a HexaDecimal number('0X'+{0to9,AtoF}): ")


"""Conversion of 3 systems to Decimal """
print ""
print "The above NumberSystem when converted to Decimal:"
print "Binary to Decimal: ",int(binary,2)
print "Octal to Decimal: ", int(octal,8)
print "HexaDecimal to Decimal: ", int(hexa_decimal,16)

"""Conversion of Decimal to 3 other NumberSystems"""
print ""
print "The Decimal number converted in to 3 other NumberSystems:"
print "Decimal to Binary: ", bin(int(decimal))
print "Decimal to Octal: ", oct(int(decimal))
print "Decimal to HexaDecimal: ", hex(int(decimal))
