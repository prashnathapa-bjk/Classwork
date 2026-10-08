student={
    "name":"John Doe",
    "age":20,
    "course":"Computer Science", 
    "marks": 78
}
print("Student Information:")
print(student)

#Increase marks by 5
student["marks"] = student["marks"] + 5

#addd status 
if student["marks"] >= 50:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"
    print("Updated Student Information:")
    print(student)

