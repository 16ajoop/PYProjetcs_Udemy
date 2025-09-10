def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)




# The code needs to print the solution to the FizzBuzz game.   

# - Your program should print each number from 1 to x where x is the input number. 
# - However when the number is divisible by 3 then instead of printing the number it should print "Fizz".   
# - When the number is divisible by 5, then instead of printing the number it should print "Buzz". 
