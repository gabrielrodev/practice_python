# Exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally
#               try:
#               Try some code if the code is dangerus
#               except Exception:
#               Handle and exception
#               Finally:
#               Do some clean up
#1 / 0 ZeroDivisionError

# 1 + "1" TypeError

# int("pizza")  ValueError

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ValueError:    #except Exception is mal practice
    print("Enter a number!")
except ZeroDivisionError:
    print("You can't divide by zero")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")