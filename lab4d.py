#!/usr/bin/env python3

# Strings 1
str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    # Returns the first five characters of the string
    return s[:5]

def last_seven(s):
    # Returns the last seven characters of the string
    return s[-7:]

def middle_number(n):
    # Converts the number to a string and returns the second and third characters
    n_str = str(n)
    return n_str[1:3]

def first_three_last_three(s1, s2):
    # Combines the first three characters of s1 with the last three characters of s2
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))         # Output: 'Hello'
    print(first_five(str2))         # Output: 'Senec'
    print(last_seven(str1))         # Output: 'World!!'
    print(last_seven(str2))         # Output: 'College'
    print(middle_number(num1))      # Output: '50'
    print(middle_number(num2))      # Output: '.5'
    print(first_three_last_three(str1, str2))  # Output: 'Helege'
    print(first_three_last_three(str2, str1))  # Output: 'Send!!'

