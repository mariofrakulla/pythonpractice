""" Problem 1--> Create an array of 5 integers and display the array items"""
from array import *
arrayNum = array('i', [1,3,5,7,9])

for i in arrayNum:
    print(i)
print("Access first three items individually")
print(arrayNum[0])
print(arrayNum[1])
print(arrayNum[2])

""" Problem 2 --> Append a number at the end of array """

arrayNum2 = array('i', [1,3,5,7,9])
print("Original array: " + str(arrayNum2))
print("Append 11 at the end of the array: ")
arrayNum2.append(11)
print("New array: " + str(arrayNum2))

""" Problem 3 --> Write a program to reverse the order of the items in the array """
arrayNum3 = array('i', [1,2,3,4,5])
print('Original array 3: ' + str(arrayNum3))
print('Reversed Array: ' + str(arrayNum3[::-1]))
""" Method 2 --> using reverse() """
arrayNum4 = array('i',[2,4,1,4,3])
print(arrayNum4)
arrayNum4.reverse()
print(arrayNum4)

""" Problem 4 --> Write a program to get the length in bytes of an array ; itemsize """
arrayNum5 = array('i', [2,3,4,1,0,21])
print('Original Array: ' + str(arrayNum5))
print('Array 5 Size: ' + str(arrayNum5.itemsize))
arrayNum6 = array('i', [21,12,123,43,4134,3,4123,123123,121])
print('Original Array: ' + str(arrayNum6))
print('Array 6 Size: ' + str(arrayNum6.itemsize))

""" Problem 5 --> Write a program to get"""
arrayNum7 = array('i', [32, 12,31,312,3333])
print('Original Array: ' + str(arrayNum7))
print('Printing array''s memory address and buffer length: ' + str(arrayNum7.buffer_info()))
print('Printing array''s memory address only: ' + str(arrayNum7.buffer_info()[0]))
""" Problem 6 --> Write a program to get number of occurrences of an element in an array """
#count
arrayNum8 = array('i', [3,4,1,2,4,2])
print('Original Array: ' + str(arrayNum8))
print('Number of occurrences of  number 2 in array 8 is: ', arrayNum8.count(2))

""" Problem 7 --> Write a Python program to append items from inerrable to the end of the array """
arrayNum9 = array('i',[1,2,3,4,5])
print(arrayNum9)
arrayNum9.extend(arrayNum9)
print(arrayNum9)

""" Problem 8 --> Write a Python program to convert an array to an array of machine values
 and return the bytes representation. """

arrayNum10 = array('i', [1,2,3,4,5])
arrayNum11 = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
s = arrayNum10.tobytes()
print(s)
m = arrayNum11.tobytes()
print(m)

""" Problem 9 --> fromlist() """
arrayNum12 = [1,2,3]
arrayNum13 = array('i', [4,5,6])
arrayNum13.fromlist(arrayNum12)
print(arrayNum13)

""" Problem 10 --> Write a Python program to insert a new item before the second element
 in an existing array"""
arrayNum13.insert(3,55)
#(position, value)
print(arrayNum13)

""" Problem 11 --> Write a Python program to remove a specified item using the
index from an array."""
arrayNum13.pop(4)
print(arrayNum13)

""" Problem 12 --> Write a Python program to remove the first occurrence of
a specified element from an array."""
""" remove() """
arrayNum15 = array('i',[1,2,3,4,5,6,67])
print(arrayNum15)
arrayNum15.remove(1)
#remove first occurrence of element
print(arrayNum15)

""" Problem 13 -->  Write a Python program to convert an array to an ordinary
 list with the same items"""
#convert an array ro a regular list
arrayNum16 = array('i', [1,3,4,5,12,332])
print(arrayNum16)
List16 = arrayNum16.tolist()
print(List16)