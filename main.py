class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)


class Employee(Person):
    def __init__(self,name,idnumber,salary):
        super().__init__(name,idnumber)  
        self.salary=salary
    def display(self):
        super().display()
        print(self.salary)

emp1=Employee("Ryan", "EM2341",40000)
emp1.display()