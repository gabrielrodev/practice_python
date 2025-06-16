#print shipping label
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
#    for value in kwargs.values():
#      print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.","Spongebob","Squarepants","III",
               street="123baba",
               pobox="bro",
               apt="100",
               city="london",
               state="MI",
               zip="54321")





"""

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123baba",
              apt="100",
              city="london",
              state="MI",
              zip="54321")

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("gabo","nomad","happy")


def add(*args):         #args is kind of like a variable almost but we have ot have the opening * to it
    total = 0           #print(type(args)) args is a tuple and kwargs is a dictionary
    for arg in args:
        total += arg
    return total
print(add(1))
"""