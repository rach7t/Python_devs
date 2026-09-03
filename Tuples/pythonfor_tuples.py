#wap to create a tuple(name, department,salary)
employee1= ("John Doe", "Engineering", 75000)
employee2= ("Jane Smith", "Marketing", 65000)
employee3= ("Alice Johnson", "Finance", 80000)


#highest salary
highest_salary = max(employee1[2], employee2[2], employee3[2])
if highest_salary == employee1[2]:
    print(f"The employee with the highest salary is {employee1[0]} from {employee1[1]} department with a salary of ${employee1[2]}.")
elif highest_salary == employee2[2]:
    print(f"The employee with the highest salary is {employee2[0]} from {employee2[1]} department with a salary of ${employee2[2]}.")
else:
    print(f"The employee with the highest salary is {employee3[0]} from {employee3[1]} department with a salary of ${employee3[2]}.")


#AVAERAGE SALARY
average_salary = (employee1[2] + employee2[2] + employee3[2]) / 3
print(f"The average salary of the employees is ${average_salary:.2f}.")


#top 2 highest salaries
salaries = [employee1[2], employee2[2], employee3[2]]
salaries.sort(reverse=True)
print(f"The top 2 highest salaries are ${salaries[0]} and ${salaries[1]}.") 

#salary greaterr than average salary
above_average_employees = []
if employee1[2] > average_salary:
    above_average_employees.append(employee1[0])
if employee2[2] > average_salary:
    above_average_employees.append(employee2[0])
if employee3[2] > average_salary:
    above_average_employees.append(employee3[0])

print(f"The employees with salaries above the average are: {', '.join(above_average_employees)}.")



#we can implement this using tuple in tuple 
employees = (
    ("John Doe", "Engineering", 75000),
    ("Jane Smith", "Marketing", 65000),
    ("Alice Johnson", "Finance", 80000)
    
)
highest_salary = max(employee[2] for employee in employees)
print(f"The highest salary is ${highest_salary}.")

#average_salary 
average_salary = sum(employee[2] for employee in employees) / len(employees)
print(f"The average salary is ${average_salary:.2f}.")