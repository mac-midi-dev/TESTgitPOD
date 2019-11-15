count_string = input("Input some text that you'd like to get the length of:")
print(len(count_string))

# even white space
my_string = "newLine 4 chars"
for letter in my_string:
    print(letter)

#
word = "abc"
print(word[0],print(word[1]),print(word[2]))    
print(word[1])    
print(word[2])



fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
for fruit in fruits:
    print(fruit)


fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
counter = 0


while counter < len(fruits):
    print(fruits[counter])
    counter += 1