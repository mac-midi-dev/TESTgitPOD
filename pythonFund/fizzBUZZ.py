#  The purpose of fizzbuzz is to iterate over a list or range of numbers, 
#  different choices that must be made depending on the value of that number.
#  If the number is divisible by 3, then we print out fizz. 
#  If the number is divisible by 5, we print out buzz. 
#  If, however, the number is divisible by both 3 and 5, print out fizzbuzz. 
#  Otherwise, we just print out the number.
#
#                           3*5=(15)fizzbuzz
#
for number in range(0, 16):
    if number == 0 :
        print(number)
        continue
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")    
    else:
        print(number)