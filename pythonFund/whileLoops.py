countdown_number = 10
print("Initiating GAME Sequence...")
print("GAME load In...")
while countdown_number >= 0:
    print(" %s seconds" % countdown_number)
    countdown_number -= 1
print("And We Have Lift Off!")

# play_game = True
# while play_game:
  #  win_number = 9
 #   number = int(input("Please enter a number:"))
#    if number > 5:
 #       print("%s Answer is greater than 5 but less than 10" % number)
 #   elif number < 5:
  #      print("%s is less than Answer" % number)
#else:
 #   print("%s is not greater than, or less than 9. Therefore, %s must be equal to Answer." % (win_number, number))
  #  print("YOU WIN")

# prints 0-9
for item in range(10):
    print(item)
# prints 5-9
for item in range(5, 10):
    print(item)
# prints 0-90 by 10s
for item in range(1, 100, 10):
    print(item-1)
# prints 20-0
for item in range(20, 0, -1):
    print(item)

        
        