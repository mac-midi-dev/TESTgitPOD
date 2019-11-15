# moonWeight is 16.5 times weaker than on earth
moonWeight = 0.165
earthPounds = 175
string = "MAC"
eval = moonWeight * earthPounds 
print("If you weigh 175lb on earth ","Then you weigh",round(eval, 2,), "pounds on the MOON")
# print(round(eval, 2))
print(type(moonWeight))
print(type(earthPounds))
# blackslash for formatting *2 muliptly string
print("Computer: \"How much does that weigh?\"" *2 )

yourWeight = input("How Much Do You Weigh?")
print("You Weigh {}".format(yourWeight))

print("You Weigh %slbs" % yourWeight )

#used round() on onMoon to display 2 digets 
yourWeight = int(input("How Much Do You Weigh?"))
onMoon = float(yourWeight * moonWeight)
print("You Weigh %s-lbs on the MOON" % round(onMoon, 2) )