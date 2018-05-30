""" W3resource """
""" Problem 1--> Write a Python function to find the Max of three numbers """
def maxOfThree(a,b,c):
    max = c
    if (b > max):
        max = b
    elif (a > max):
        max = a
    return  max
print(maxOfThree(0,1,3))

""" Problem 2 --> Write a Python function to sum all the numbers in a list. """

def sumList(List1):
    sum = 0
    for i in List1:
        sum = sum + i
    return  sum
m = [1,2,3,4]
print(sumList(m))

""" Problem 3 --> Write a Python function to multiply all the numbers in a list. """
def prodList(List2):
    prod = 1
    for j in List2:
        prod = prod * j
    return prod
print(prodList(m))

""" Problem 4 --> Write a Python program to reverse a string. """

def reverseString(str):
    print(str[::-1])
str1 = 'Mario'
reverseString(str1)

""" Problem 5 -->  Write a Python function to calculate the factorial of a number (a non-negative integer). 
The function accepts the number as an argument"""

def factorialComp(num):
    factorial = 1
    for m in range(1,num+1):
        factorial = factorial * m
    return factorial
print(factorialComp(5))

""" Problem 6 --> Write a Python function to check whether a number is in a given range. """
def checkRange(m):
    if m in range(3, 11):
        print(m, ' is in the range')
checkRange(7)

""" Problem 7 --> Write a Python function that accepts a string and calculate the number of upper 
case letters and lower case letters"""
def countUpperLower(string2):
    upper = 0
    lower = 0
    for i in string2:

        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower +1
    print('There are', upper, ' upper case letters and ', lower, ' lower case letters')
countUpperLower('Mario Frakulla')

""" Problem 8 --> Write a Python function that takes a list and returns a new list with unique elements 
of the first list. """

def countUnique(string3):
    uniqueList = []
    for itt in string3:
        if itt not in uniqueList:
            uniqueList.append(itt)
    print(uniqueList)
listt = [1,2,2,3,4,4,5]
countUnique(listt)

""" Problem 9 -->  Write a Python function that takes a number as a parameter and check 
the number is prime or not"""
import  math
def checkPrime(prime):
    for itn in range(2,round(math.sqrt(prime))):
        if prime % itn == 0:
            print(prime, ' is not a prime number')
            quit()
        else:
            print(prime, ' is a prime number')
checkPrime(17)

""" Problem 11 -->  Write a Python function to check whether a number is perfect or not """

def checkPerfect(num2):
    divisors = []
    for im in range(1,num2):
        if num2 % im == 0:
            divisors.append(im)
    sumLis = sum(divisors)
    if sumLis == num2:
        print(num2, ' is a perfect number')
checkPerfect(6)
""" Problem 12 --> Write a Python function that checks whether a passed string is palindrome or not."""
def PalindromeCheck(string4):
    if string4 == string4[::-1]:
        print('The string is Palindrome')
    else:
        print('The string is not Palindrome')
PalindromeCheck('Mario')
PalindromeCheck('aamaa')

""" Problem 13 -->  Write a Python function that prints out the first n rows of Pascal's triangle. """
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow =[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(10)

""" Problem 14 --> Write a Python function to check whether a string is a pangram or not """
import string, sys
def ispanagram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
print(ispanagram('The quick brown fox jumps over the lazy dog'))

""" Problem 15 -->  Write a Python program that accepts a hyphen-separated sequence of words as input and 
prints the words in a hyphen-separated sequence after sorting them alphabetically. """
def separHyp(strng):
    strngSet = set(strng.split('-'))
    sortedStrng = sorted(strngSet)
    print('-'.join(sortedStrng))
stringHyp = 'red-black-green-yellow-magenta-blue-white'
separHyp(stringHyp)
""" Problem 18 --> Write a program to execute a string containing Python code """

codeOne = 'print("hello world")'
codeTwo = "print('Multiply of 2 and 3 is: ', 2*3)"
exec(codeOne)
exec(codeTwo)

""" Problem 20 --> Write a Python program to detect the number of
 local variables declared in a function."""
def abc():
    x = 1
    y = 2
    str1 = "w3resource"
    print("Python Exercises")

print(abc.__code__.co_nlocals)





