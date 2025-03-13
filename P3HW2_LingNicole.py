# Nicole Ling
# 03/13/2025
# P3HW2
# Determine OT pay, regular pay, and gross pay

"""
Pseudocode:

Get employee_name from user (need a variable, use input() function)
Get hours_worked from user (need variable, use input(), use float())
Get pay_rate from user (need variable, use input(), use float())

Determine if employee worked any overtime:

if hours_worked > 40:
    Calculate OT_hours_worked (hours_worked - 40) - create new variable
    Calculate OT_pay_rate (pay_rate * 1.5) - create variable
    Calculate OT_pay (OT_hours_worked * OT_pay_rate) - create variable
    Calculate reg_pay (40 * pay_rate) - create variable
    Calculate gross_pay (reg_pay + OT_pay) - create variable

# hours_worked <= 40
else: 
    Calculate OT_hours_worked = 0
    Calculate OT_pay = 0
    Calculate reg_pay (hours_worked * pay_rate)
    Calculate gross_pay = reg_pay

Output the values
Display employee name separately
Display all headings(formatted) 
Display dotted line
Display corresponding values (formatted)

# Display the values in columns
print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'Overtime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
print("-"*50)
print(f"{hours_worked:<20}${pay_rate:<20.2f}")

"""
# Get employee and pay information

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("-"*50)
print("Employee name: ", employee_name)
print()

# Calculate pay

OT_hours_worked = (hours_worked - 40)
OT_pay_rate = (pay_rate * 1.5)
OT_pay = (OT_hours_worked * OT_pay_rate)
reg_pay = (hours_worked * pay_rate)
gross_pay = (reg_pay + OT_pay)

if hours_worked > 40:
    OT_hours_worked = (hours_worked - 40)
    OT_pay_rate = (pay_rate * 1.5) 
    OT_pay = (OT_hours_worked * OT_pay_rate) 
    reg_pay = (40 * pay_rate) 
    gross_pay = (reg_pay + OT_pay)

# hours_worked <= 40
else: 
    OT_hours_worked = 0
    OT_pay = 0
    reg_pay (hours_worked * pay_rate)
    gross_pay = reg_pay

# Display the values in columns

print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'Overtime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
print("-"*50)
print(f"{hours_worked:<20}${pay_rate:<20.2f}{OT_hours_worked:<20}${OT_pay_rate:<20.2f}${reg_pay:<20.2f}${gross_pay:<20.2f}")
