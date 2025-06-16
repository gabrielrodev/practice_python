#variable scope
# (LEGB) local -> enclosed -> global -> built-in
# it goes in order first searches on local and so on
from math import e #built-in

def character(): #local
    print("Russel")
    def character_friends(): #enclosed
        characters = ["gabo, john, rash, max"]
        print(characters)

print(character) #global