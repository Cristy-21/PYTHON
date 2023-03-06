#Define a fizzbuzz function that accepts a single number as an argument. The function should print every number from 1 to that argument. 

#If the number is divisible by 3, print "Fizz" instead of the number.

# If the number is divisible by 5, print "Buzz" instead of the number.

#If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.

#If the number is not divisible by either 3 or 5, just print the number.



def fizzbuzz(number):
    number1=int(1)
    while number1<=number:
        if number1%3==0 and number1%5==0:
            print("FizzBuzz")  
        elif number1%3==0:
            print("Fizz")
        elif number1%5==0:
            print("Buzz")
        else:
            print(number1)
        number1+=1

fizzbuzz(30)  
           
