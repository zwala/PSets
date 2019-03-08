
            
inputString = 'azcbobobegghakl'

prevChar = ""
currentString = ""
longestString = ""

for char in inputString:
    if prevChar <= char:
        currentString += char
        if len(currentString) > len(longestString):
            longestString = currentString
    else:
        currentString = char
    prevChar = char
print('Longest substring in alphabetical order is: ' + longestString )

      