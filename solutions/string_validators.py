# URL: https://www.hackerrank.com/challenges/string-validators/problem

"""
str.isalnum(): This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha(): This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit(): This method checks if all the characters of a string are digits (0-9).

str.islower(): This method checks if all the characters of a string are lowercase characters (a-z).

str.isupper(): This method checks if all the characters of a string are uppercase characters (A-Z).
 
"""

if __name__ == '__main__':
    s = input()

    
def string_validators(s):
    print (any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
  
string_validators(s)
    




