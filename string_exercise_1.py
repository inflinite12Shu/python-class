# -*- coding: utf-8 -*-
"""String_Exercise_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12zkk5bl-OgEHsp7dVI9srd6mKHSqjkKj

**Exercise 1: Create a string made of the first, middle and last character**

Write a program to create a new string made of an input string’s first, middle, and last character.

Given:

str1 = James

Case 2 = Laptop
"""

def new_string(str1):
    f_str = str1[0]
    m_str = str1[2]
    l_str = str1[-1]
    return f_str + m_str + l_str

str1 = "James"
print(new_string(str1))

def new_string(str1):
    f_str = str1[0]
    m_str = str1[2]
    sm_str = str1[3]
    l_str = str1[-1]
    return f_str + m_str + sm_str + l_str

str1 = "Laptop"
print(new_string(str1))

"""**Exercise 2: Create a string made of the middle three characters**

Write a program to create a new string made of the middle three characters of an input string.

Given:

Case 1   
str1 = JhonDipPeta

Case 2 = Exercise
"""

pass
str1 = "JhonDipPeta"
print(str1[4:7])

"""**Exercise 3: Create a new string made of the first, middle, and last characters of each input string**
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Given:

s1 = America

s2 = Japan
"""

def string(s1, s2):
   first_string1 = s1[0] 
   secend_string1 = s1[3] 
   thrend_string1 = s1[6]
   first_string2 = s2[0] 
   scend_string2 = s2[2] 
   thrend_string2 = s2[4]
   return  first_string1 + secend_string1 + thrend_string1 + first_string2 + scend_string2 + thrend_string2

s1 = "America"
s2 = "Japan"

print(string(s1, s2))

"""**Exercise 4: Convert String character into uppercase

Given:
python
"""

pass
py = "python"
print(py.upper())

"""**Exercise 5: Convert string into lower case.

Given : PYTHON
"""

pass
py = "PYTHON"
print(py.lower())

"""#**Exercise 6: Count number of "S" in the string.**

Given: She Sells sea shells by the sea shores.
"""

pass
sen = "She Sells sea shells by the sea shores."
print(sen.count("s"))

"""# **Exercise 7: Join two strings**



**Given:**

Case 1:

s1 = "Yn"
s2 = "PYnative"

Case 2:

s1 = "Ynf"
s2 = "PYnative
"""

pass
s1 = "Yn"
s2 = "PYnative"

s = s1 + s2
print(s)

s1 = "Ynf"
s2 = "PYnative"

s = s1 + s2
print(s)

"""**Exercise 8: Find all occurrences of a substring in a given string by ignoring the case**

Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:

str1 = "Welcome to USA. usa awesome, isn't it?"
"""

str1 = "Welcome to USA. usa awesome, isn't it?"

substring = "USA"

count = str1.upper().count(substring.upper())

print(count)

str1 = "Welcome to USA. usa awesome, isn't it?"
print(str1.count("USA"))

"""**Exercise 9: Reverse a given string**

Given:

str1 = PYnative

Str 2 = Badin

Str 3 = Pakistan
"""

pass
str1 = "PYnative"
str2 = "Badin"
str3 = "Pakistan"


print(str1[::-1])
print(str2[::-1])
print(str3[::-1])

"""**Exercise 10: Find the  position of a given substring**

Write a program to find the  position of a substring “Emma” in a given string.

Given:

str1 = "Emma is a data scientist who knows Python. 
"""

pass
str1 = "Emma is a data scientist who knows Python."
print(str1.find("Emma"))

"""**Exercise 11: Split a string on hyphens**

Write a program to split a given string on hyphens and display each substring.

Given:

str1 = Emma-is-a-data-scientist
"""

pass
str1 = "Emma-is-a-data-scientist"
print(str1.split("-"))