# math-case statements are alternatives to using many elif statement. is cleaner

def is_weekend(day):
    match day: # | means or
        case "Monday"|"Wednesday"|"Tuesday"|"Friday"|"Thursday":
            return False
        case "Sunday"|"Saturday":
            return True
        case _:
            return False
# match is like extra to start using cases which i think is like. match day to case 1 and so on. _ is if all the others are not used
print(is_weekend("Saturday"))