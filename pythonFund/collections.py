# SLICE
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[0:2])
print(fruits[:2])
print(fruits[4:])
print(fruits[ : ])
print(fruits[0:4:2])   # start0_stop4_by2s
print(fruits[::-1])   # ierrate backwards

name="MAC"
age="29"
print("%s is %s years old" % (name, age))


my_tuple = ("Hello", "World")
print(my_tuple[1])

my_tuple = ("Hello", "World", "MAC1")
for item in my_tuple:
    print(item)


usernames = ["tombombadil", "BilboBaggins", "Frodo_Baggins"]
usernames.append("MACmidiDev")
for username in usernames:
    print(username)

# tuples are IMMUTEABLE
user = ("tombombadil", "Tom", "Bombadil")
print("\tUsername  : %s" % user[0])
print("\tFirst Name: %s" % user[1])
print("\tLast Name : %s" % user[2])
#    print("Last Name : %s" % user[3])

lots_of_numbers_tuple = tuple(i for i in range(1000))
print(lots_of_numbers_tuple[515:776])

letters = ["a","s","d","f","g","h","j","k","l","q","w","e","z","x","c","v"]
letters.sort()
del letters[0]
print(letters)


my_word = "Hello"
print(my_word.upper())
my_uppercase_word = my_word.upper()
print(my_uppercase_word)

# replaces 1-10 with sqrt of 1-10
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
while i < len(mylist):
    mylist[i] = mylist[i]**2
    i += 1
print(mylist)




