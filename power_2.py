# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two

x=int(input("input a value "))

if x !=0 and x & (x-1)==0:
     print(str(x)+"==>"+str(True))

else:
    print(str(x)+"==>"+str(False))