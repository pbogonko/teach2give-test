# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
# "FizzBuzz"
count=0
while(count<100):
    count+=1
    if(count%3==0 and count%5==0):
        print(str(count)+":FizzBuzz")
    elif(count%5==0):
        print(str(count)+":Buzz") 
    elif(count%3==0):
        print(str(count) +":Fizz")     
    else :
        print(count)

     
