"""String Problems"""

""" Problem 1--> Calculate the length of a string """
stringOne = "Mario Frakulla"
#Method 1
print(len(stringOne))
#Method 2
length = 0
for i in stringOne:
    length = length + 1
print(length)
"""Problem 2--> Character frequency in a string"""
"""Dictonaries; {key:value}"""
def char_frequency(str1):
    dict={}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return  dict
print(char_frequency('google.com'))
""" Problem 3 """
def printProgram(string1):
    if len(string1)<2:
        return ''
    else:
        newString = string1[0]+string1[1]+ string1[-2]+string1[-1]
        return newString
print(printProgram("mario"))

""" Problem 4-->  Write a Python program to get a string from a given string 
where all occurrences of its first char have been changed to '$', except the first 
char itself."""

string2 = "restart"

for i in range(1,len(string2)):

    if string2[i] == string2[0]:
        str1 = string2.replace(string2[0],'$')
        newstring = string2[0] + str1[1:]
print(newstring)

""" Problem 5--> Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string. """
def Problem5(stringOne, stringTwo):
    tempstr = stringOne[0:2]
    newOne = stringOne.replace(tempstr, stringTwo[0:2])
    newTwo = stringTwo.replace(stringTwo[0:2], tempstr)
    newstring = newOne + " " + newTwo
    return  newstring
print(Problem5('abc', 'xyz'))

""" Problem 6--> Write a Python program to add 'ing' at the end of a given string 
(length should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead. If the string length of the given string is less than 3, leave it unchanged"""

def Problem6(stringProblem6):
    if len(stringProblem6) < 3:
        return stringProblem6
    else:
        if stringProblem6[-3:] == "ing":
            newString = stringProblem6 + 'ly'
            return newString
        else:
            newString = stringProblem6 + 'ing'
            return newString
print(Problem6("trapp"))
""" Problem 8 -->  Write a Python function that takes a
 list of words and returns the length of the longest one. """
def Problem8(one, two, three, four, five, six):
    stringLength = [len(one), len(two), len(three), len(four), len(five), len(six)]
    longest = max(stringLength)
    return longest
print(Problem8("mar",'mario','1','33','33333', 'ma'))
""" Problem 8 --> input is list of strings"""
def ProblemM2(words_list):
    wordlen =[]
    for n in words_list:
        wordlen.append(len(n))
    wordlen.sort()
    return wordlen[-1]
print(ProblemM2(['1','22','mario']))
""" Problem 10 -->Exchange the first and last characters """
def Problem10(strng):
    newstring = strng[-1] + strng[1:-1] + strng[0]
    return  newstring
print(Problem10("mario"))

def Problem11(stringLong):
    result =""
    for it in range(0, len(stringLong)):
        if it%2 == 0:
            result = result + stringLong[it]
    return result
print(Problem11('abcdef'))

""" Problem12 --> Count number of word occurences in a sentence"""
def OccurencesSentence(sentence):
    newSen = sentence.split(' ')
    dict = {}
    for i in newSen:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(OccurencesSentence("Mario Frakulla Mario"))

def sortListStrings(stringIn):
    newstr = stringIn.split(',')
    m = sorted(newstr)
    return m
print(sortListStrings("red,white,black,green,black"))

""" Problem 20 --> Write a Python function to reverses a string if it's length 
is a multiple of 4 """

def rev4(strang):
    if len(strang) %4 == 0:
        newstrang = strang[::-1]
        return newstrang
    else:
        return strang

print(rev4("Mari"))

""" Problem 22 --> remove endline from a string """
newStr = "This string contains an endline\n"
print(newStr)
print(newStr.rstrip())
""" Problem 24--> Check if a string starts with a specific character """
""" use startswith() """
stranf = "Mario Frakulla"
print(stranf.startswith('M'))
""" Problem 25 --> Write a program to create a Ceasar encryption """
""" inputs are string and shift parameter"""
""" create a program that would decrypt any C cipher code"""



""" Brute Force approach """

import textwrap

sampleText = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java
'''

#textwrap.fill to manage the width of text
print()
print(textwrap.fill(sampleText, width = 50))
print(textwrap.fill(sampleText, width = 100))
textWithoutInd = textwrap.dedent(sampleText)
print()
print(textWithoutInd)

""" Count occurrences of a substring in a string """
str1 = "The quick brown fox jumps over the lazy dog"
print()
print(str1.count("fox"))
print()
""" Write a program to reverse words in a string """
wordSet = str1.split(' ')
reversedSet = []
for word in wordSet:
    revword = word[::-1]
    reversedSet.append(revword)
print(reversedSet)

""" Write a program to strip a set of characters from a string """
#want to print a character only if it's not in the character list we enter in the program

def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)
#stripping of all the vowels
print(strip_chars("The quick brown fox jumps over the lazy dog", "aeiou"))
print()

"""Write a pyhon program to count character occurence
1-Using Dictionaries"""
def countChars(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(countChars("The quick brown fox jumps over the lazy dog"))

""" squared = u00b2 """
""" cube = ub00b3; formati(area, decimals) """
area = 1256.66
volume = 1254.6632
decimals = 2
print("The area of the rectangle {0:.{1}f}cm\u00b2".format(area,decimals))
""" Write a program to print the index of the current character in a string"""
sampleString = "W3resource"
currentIndx = 0
for ind in sampleString:
    print("Current character %s, position at %d" %(ind,currentIndx))
    currentIndx = currentIndx + 1

""" split a string based on occurrence number of the delimiter """
#split at delimiter 3rd , delimiter
string ="w,3,r,e,s,o,u,r,c,e"
print(string.rsplit(',',3))






