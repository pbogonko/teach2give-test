# Write a program that takes an integer as input and returns an integer with reversed digit
# ordering.
def reverse_integer(num):
    x = str(num)[::-1]
    reverse = int(x)
    return reverse


input_num = int(input("Enter a number: "))
res = reverse_integer(input_num)
print("Reversed number:", res)