""" 
WEEK 2 – INTEGRATED DATA STRUCTURES CHALLENGE

You are given a list of student records. Each record is a tuple of the form:   (roll_number, name, marks)

students = [
    (101, "Amit", 85),
    (102, "Riya", 92),
    (103, "John", 85),
    (104, "Sara", 76),
    (105, "Riya", 92),
    (106, "Amit", 70),
    (101, "Amit", 88)   # Duplicate roll number (data error)
]

Perform the following tasks:

1. Remove duplicate records based on roll number.
   - Roll number uniquely identifies a student.
   - If duplicate roll number appears, keep only the first occurrence.

2. Find all toppers.
   - If multiple students have the highest marks, include all of them.

3. Compute the class average marks.
   - Use only the cleaned (duplicate-removed) data.

4. Create a dictionary:
       Key   → Student name
       Value → Total marks scored by that name
   - If a name appears multiple times, sum their marks.

5. Using a set, print all distinct student names.

Constraints:
- Do not use external libraries.
- Use only basic Python data structures (list, tuple, set, dictionary).
- Handle edge cases properly.
"""

students = [
    (101, "Amit", 85),
    (102, "Riya", 92),
    (103, "John", 85),
    (104, "Sara", 76),
    (105, "Riya", 92),
    (106, "Amit", 70),
    (101, "Amit", 88)   # Duplicate roll number (data error)
]
# 1
unique_students=[]
seen_roll=set()
for student in students:
    roll=student[0]
    if roll not in seen_roll:
        seen_roll.add(roll)
        unique_students.append(student)
print(unique_students)

# 2

toppers=[unique_students[0]]
maxmarks=unique_students[0][2]
for student in unique_students[1:]:
    if student[2]>maxmarks:
        maxmarks=student[2]
        toppers=[student]
    elif student[2] == maxmarks:
        toppers.append(student)
print(toppers)

#3
total_marks=0
total_marks=sum(student[2] for student in unique_students)
avg=total_marks/len(unique_students)
print(avg)

#4
name_totals={}
for student in unique_students:
    name=student[1]
    marks=student[2]
    name_totals[name]=name_totals.get(name,0)+marks
print(name_totals)

#5
distinct_names=set(student[1] for student in unique_students)
print(distinct_names)