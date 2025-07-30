# Nested class = A class defined within another class
#                   class Outer:
#                      class Inner:

#Benefits: Allows you to logically group classes that are closely related
#          Encapsulates private details that aren't relevant outside of the outer class
#          keeps the namespace clean; reduces the possibility of naming conflicts


class Company: #self means the class that is currently in used
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees] #called list comprehension(i call it list)

company1 = Company("krusty krab")
company2 = Company("chum bucket")

company1.add_employee("Eugene", "Manager")
company1.add_employee("sponge_bob", "cook")
company1.add_employee("squidward", "cashier")

company2.add_employee("sheldon","crook")
company2.add_employee("karen", "assistant")




for employee in company2.list_employees():
    print(employee)




"""class Employee:
    print("this is class youtuber")

class Employee:
    print("this is the class twitch streamer")""" #bad way to do classes

