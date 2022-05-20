name = input("Your Name is:")
print(name[0:4])
print(name[(len(name)-1)])

message = "weLcome to KiT"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.casefold())

#Centering the string
print(message.center(25,"$"))
print(message.center(50))
#Finding index
print(message.find("weLcome"))
print(message.find("KiT"))
print(message.find("afdf"))
#True or False based on the existence of the search string
print("KiT" in message)
print("z" in message)

# To replace the part of text in the given string
message2 = message.replace("KiT", "KIT")
print(message)
print(message2)