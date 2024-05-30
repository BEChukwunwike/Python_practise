first_list = ["Blessing", "Emmanuel", "Henry"]
second_list = ["Blessing", "Emmanuel", "Henry"]
third_list = second_list

print(first_list == second_list)
print(first_list is second_list)
print(third_list is second_list)


classmates = ["Chinedu", "Audu", "Olamide", "Ene"]

study_group = classmates #creating an alias

study_group.append("Fatima") #modifying the list through one of the references

print(classmates)

def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

original_list = [1, 2, 2, 3, 4, 4, 5]


unique_list = remove_duplicates(original_list)

print(unique_list)  # Output: [1, 2, 3, 4, 5]
