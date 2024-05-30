students_courses= {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}
def invert_dict(d):
    inverse={}
    for student, courses in d.items():
        for course in courses:
            if course in inverse:
                inverse[course].append(student)
            else:
                inverse[course] = [student]
                
    return inverse
print(invert_dict(students_courses))