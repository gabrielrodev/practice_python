
import time

my_time = int(input("Enter the time in seconds:"))

for x in reversed(range(0, my_time)): #You cam also do range(my_time, 0, -1)
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) # we excluded % 24 because we are not actually looking to write days
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # I'm unsure how this works exactly
    time.sleep(1)

print(f"Your timer of {my_time}s is up!")

"""
import time

#My version of the code practice

timer_seconds = int(input("Please enter the amount of seconds: "))
                print(f"hh:mm:{timer_seconds}")
timer_minutes = int(input("Please enter the amount of minutes: "))
                print(f"hh:{timer_minutes}:{timer_seconds}")
timer_hours = int(input("Please enter the amount of hours: "))
                print(f"hh:{timer_hours}:{timer_minutes}:{timer_seconds}")
                
still making it 
"""





