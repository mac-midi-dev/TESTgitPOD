# break and continue WHILEloop
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
counter = 0
while counter <= len(fruits) - 1:
    if fruits[counter] == "peach":
        break
    print(fruits[counter])
    counter += 1
print("Iteration has been completed")   


# break and continue FORloop * stops at peach-- prints(apple, banna)
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
counter = 0
for fruit in fruits:
    if fruit == "peach":
        break
    print(fruit)
print("Iteration has been completed")



# break and continue FORloop * skips over peach-- prints(0,1,3,4,5)
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
counter = 0
while counter < len(fruits):
    if fruits[counter] == "peach":
        counter += 1
        continue
    print(fruits[counter])
    counter += 1
print("Iteration has been completed")




# 99 BOOTLES of BEER on the WALL
for number in range(99, 0, -1):
    count = 0
    if count < 1:
        line_one = "{0} bottle(s) of beer on the wall. {0} bottle(s) of beer"
        line_two = "Take one down, pass it around. {0} BOOTLE of beer on the wall\n"
        
    else :
        line_one = "{0} bottle of beer on the wall. {0} bottle of beer"
        line_two = "Take one down, pass it around. {0} bottle of beer on the wall\n"

    print(line_one.format(number))
    print(line_two.format(number - 1))