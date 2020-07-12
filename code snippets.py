#Assigning elements to different lists

students=["Rohan","Naman","Mohit","Abhishek"]
teachers=["Prateek","Vijay","Soumya","Devi"]
print ("The names of students are",students)
print ("The names of teachers are",teachers)
students.append("Pranav")
teachers.append("Vinny")
print ("The updated student list is",students)
print ("The updated teacher list is",teachers)


#Accessing elements from a tuple

students=("Rohan", "Naman", "Pranav")
print("The students present today are",students)
print("The 3rd student name is",students[2])


#Deleting different dictionary elements

pairs={"Pranav":"Vinny", "Naman":"Vijay","Rohan":"Devi"}

print("The student assigned to each teacher is",pairs)
del pairs["Rohan"]

print("The updated pairs are",pairs)
