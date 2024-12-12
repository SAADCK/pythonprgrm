class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary
        self.da = 0.0
        self.hra = 0.0
        self.pf = 0.0
        self.net_salary = 0.0

    def calculate_components(self):
        # Assuming DA, HRA, and PF percentages
        da_percentage = 0.10  # 10% of basic salary
        hra_percentage = 0.15  # 15% of basic salary
        pf_percentage = 0.12  # 12% of basic salary

        # Calculate each component
        self.da = self.basic_salary * da_percentage
        self.hra = self.basic_salary * hra_percentage
        self.pf = self.basic_salary * pf_percentage
        self.net_salary = self.basic_salary + self.da + self.hra - self.pf

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"DA (10%): {self.da}")
        print(f"HRA (15%): {self.hra}")
        print(f"PF (12%): {self.pf}")
        print(f"Net Salary: {self.net_salary}")

# Example usage
employee_name = input("Enter the employee's name: ")
basic_salary = float(input("Enter the basic salary: "))
employee = Employee(employee_name, basic_salary)
employee.calculate_components()
employee.display_details()
