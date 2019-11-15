def check_engine(oil, coolant, gasoline):
   # Check your engine!
   if oil:
       if not gasoline:
         return "gas issue"
       elif not coolant:
         return "coolant issue"
       elif not coolant and not gasoline:
         return "gas and coolant issue"
       else:
         return "engine started"
   elif not oil:
     return "oil issue"
   else:
     return "Poof...CAR, Started!"
# Check your code by experimenting with the
# values of oil, coolant and gasoline here
oil = 0
coolant = 1
gasoline = 1
print(check_engine(oil, coolant, gasoline))

oil = 1
coolant = 0
gasoline = 1
print(check_engine(oil, coolant, gasoline))

oil = 1
coolant = 1
gasoline = 0
print(check_engine(oil, coolant, gasoline))

oil = 1
coolant = 0
gasoline = 0
print(check_engine(oil, coolant, gasoline))


# tinearyOperator shorthand
my_boolean = False

print(my_string = "Hello" if my_boolean else "World")

if my_boolean:
  my_string = "Hello"
else:
  my_string = "World"

print(my_string)