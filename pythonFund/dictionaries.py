user = {
    "fName":"MAC",
    " lName":"midi",
    "username":"   Dev",
    " age":"29",
} 


print(user)
print(user["username"])
print(user["fName"])
print(user[" lName"])
print(user[" age"])
print(user)


for key, value in user.items():
    print("--------------")    
    print("Key: %s" % key )
    print("Value: %s" % value)
print("-------------")    