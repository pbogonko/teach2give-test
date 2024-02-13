# Write a program that accepts a string as input, capitalizes the first letter of each word in the
# string, and then returns the result string.

def myfunc(str):
    
    return str.title()

str = input("Enter a string: ")
result = myfunc(str)
print("Result:", result)