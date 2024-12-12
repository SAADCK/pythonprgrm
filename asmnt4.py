
def calculate_salary(basic_salary):
    # Calculate components
    DA = 0.12 * basic_salary       # 10% of basic salary
    HRA = 0.7 * basic_salary       # 15% of basic salary
    PF = 0.05 * basic_salary        # 5% of basic salary
    
    # Calculate net salary
    net_salary = basic_salary + DA + HRA - PF
    return DA, HRA, PF, net_salary

# Get employee details
name = input("Enter Employee Name: ")
designation = input("Enter Employee Designation: ")
basic_salary = float(input("Enter Basic Salary: "))

# Calculate salary components
DA, HRA, PF, net_salary = calculate_salary(basic_salary)

print("\nEmployee Details:")
print(f"Name           : {name}")
print(f"Designation    : {designation}")
print(f"Basic Salary   : {basic_salary:.2f}")
print(f"DA             : {DA:.2f}")
print(f"HRA            : {HRA:.2f}")
print(f"PF             : {PF:.2f}")
print(f"Net Salary     : {net_salary:.2f}")
