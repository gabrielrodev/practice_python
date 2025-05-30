# Dictionary: {key:definition} first you print were you want it store then you print what is the value

capitals = { "USA" : "Washington D.C.",
             "India" : "New Delhi",
             "Venezuela" : "Caracas",
             "United Kingdom" : "London"
}
#print(dir(capitals)
#print(help(capitals)
#capitals.get("USA")

#if capitals.get("Japan"):
#    print("That capital exists")
#else:
#    print("That capital does not exist")

#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Detroit"})
#capitals.pop("USA")
#capitals.popitem()
#capitals.clear()
#keys = capitals.keys()
#print(keys)

#keys = capitals.keys()

#for key in capitals.keys():
    #print(key)

#values = capitals.values()
#for value in capitals.values():
#print(value)

#items = capitals.items()
print("--------------------")
print("country : capitals")
print("--------------------")
for key, value in capitals.items():
    print(f"{key}: {value}")