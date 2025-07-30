# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as a argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs): #needed to use after @ instead of when you called first
        print("You add fudge")
        func(*args, **kwargs) # args and kwargs is to accept any input
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

get_ice_cream("vanilla") # calls its function and also adds the two decorators 