my_variable = True

if my_variable:
    print("This condition is True")
    print("ABC")
    print("DEF")
print("WTF")    


## ---------------------------------------------------LOGICAL OPERATORS
# not keyword 
exit_program = False
if not exit_program:
    print("This program will not exit just yet")
else:
    print("This program will now be terminated...")
# and keyword
exit_program = True
critical_systems_shutdown = True
if exit_program and critical_systems_shutdown:
    print("Safely terminating program...")
else:
    print("This program will not exit just yet")
# or keyword
exit_program = False
manual_override = True
if exit_program or manual_override:
    print("This program will now be terminated...")
else:
    print("This program will not exit just yet")
# nestingConditions
exit_program = True
manual_override = False
critical_systems_shutdown = False
if not exit_program and not critical_systems_shutdown:
    if manual_override:
        print("Shutting system down manually")
    else:
        print("This program will not exit just yet")
elif exit_program and critical_systems_shutdown is not True:
    print("Critical systems must be safely shut down before exiting the program")
else:
    print("This program will now be terminated...")    
## ---------------------------------------------------LOGICAL OPERATORS



# IF.else
print("Number GAME 1")
number = int(input("Please enter a number:"))
if number == 5:
    print("%s is equal to 5" % number)
else:
    print("%s is not equal to 5" % number)

# If.Elif.Else
print("Number GAME 2")
number = int(input("Please enter a number:"))
if number > 5:
    print("%s is greater than 5" % number)
elif number < 5:
    print("%s is less than 5" % number)
else:
    print("%s is not greater than, or less than 5. Therefore, %s must be equal to 5." % (number, number))