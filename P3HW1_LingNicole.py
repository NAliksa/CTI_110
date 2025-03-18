# Nicole Ling
# P3HW1
# 03/18/2025
# 

# Input grades

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print()

# add grades to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
sum = mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6
lowest_grade = min(grades)
highest_grade = max(grades)
avg = sum / 6

# Display results

print("-"*12, "Results", "-"*12)
print("Lowest Grade: ", lowest_grade)
print("Highest Grade: ", highest_grade)
print("Sum of Grades: ", (sum))
print("Average: ", f'{sum / 6:.2f}')
print("-"*35)

# Determine letter grade for average

if avg >= 90:
    print('Your grade is: A') 
    
elif avg >= 80:
    print('Your grade is: B')

elif avg >= 70:
    print('Your grade is: C') 

elif avg >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F')
