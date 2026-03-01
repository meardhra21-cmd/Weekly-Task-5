class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary()")

    def display_details(self):
        print("Employee Name:", self.name)
        print("Final Salary:", self.calculate_salary())
        print("-" * 30)


class Manager(Employee):
    def calculate_salary(self):
        bonus = self.base_salary * 0.20  # 20% bonus
        allowance = 5000
        return self.base_salary + bonus + allowance


class Developer(Employee):
    def calculate_salary(self):
        project_bonus = self.base_salary * 0.10  # 10% project bonus
        return self.base_salary + project_bonus


class Intern(Employee):
    def calculate_salary(self):
        stipend = 15000  # Fixed stipend
        return stipend


manager = Manager("Anita", 80000)
developer = Developer("Rahul", 60000)
intern = Intern("Sneha", 20000)

manager.display_details()
developer.display_details()
intern.display_details()
