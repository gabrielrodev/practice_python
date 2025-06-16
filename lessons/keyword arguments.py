
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1,area=123,first=456,last=231)
print(phone_num)

#print("1","2","3","4","5","6","7","8","9", sep="-") # another example of key arguments


"""
for x in range(1, 11):
    print(x, end=" ") # end is a keyword argument
"""
"""
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")
hello("hi", title="Ph", last="mob", first="clock") #positional argument fist before keyword argument
"""


# or you can do like hello("Hi","DC", "cold", "duck")