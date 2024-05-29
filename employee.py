employee_names = ["Chinedu", "Adaeze", "Aliyu", "Ngozi", "Adebayo", "Hassan", "Gambo", "Ifeoma", "Olamide", "Godiya"]

subList1 = employee_names[:5]
subList2 = employee_names[5:]

print(subList1)
print(subList2)

subList2.append("Kriti Brown")

del subList1[1]

merged_list= subList1 + subList2

salaryList= [80000, 85000, 90000, 93000, 88000, 95000, 84000, 91000, 94000, 81000]

for salary in range(len(salaryList)):
    salaryList[salary] += salaryList[salary] *0.04

salaryList.sort()

top3_salaries = salaryList[-3:]

print("Merged Employee list:", merged_list)
print("Updated salary list:", salaryList)
print("Top 3 salaries:", top3_salaries)
