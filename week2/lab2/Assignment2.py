Student_Record = {}
Student_Record['Stdid'] = ['std101','std102','std103','std104','std105','std106','std107','std108','std109','std110']
Student_Record['Stdname'] = ['Ashish kumar','Abhishek kumar','Aman','Rahul','Ruby','Suamn','Saurabh','sumit','Kamlesh','Rohan']
Student_Record['Age'] = [15,14,15,14,13,13,15,14,15,15]
Student_Record['Maths'] = [87,48,78,45,89,67,34,67,78,24]
Student_Record['English'] = [89,45,56,67,67,46,23,45,56,12]
Student_Record['Hindi'] = [67,85,23,45,89,90,45,23,45,34]
Student_Record['Computer'] = [90,45,67,56,65,67,34,90,67,56]
Student_Record['Science'] = [89,90,78,45,93,67,45,78,99,45]

print("Student Record: ")
print("S no.   ID             Name            Age     Maths     English  Hindi    Computer Science")
for i in range(len(Student_Record['Stdid'])):
    print(f"{i+1:<6} {Student_Record['Stdid'][i]:<15} {Student_Record['Stdname'][i]:<15} {Student_Record['Age'][i]:<8} {Student_Record['Maths'][i]:<8} {Student_Record['English'][i]:<8} {Student_Record['Hindi'][i]:<8} {Student_Record['Computer'][i]:<8} {Student_Record['Science'][i]:<8}")

# Name and Age of students with more than 50 marks in English
print("\nStudents with more than 50 marks in english:")
print("Name            Age")
for i in range(len(Student_Record['Stdid'])):
    if(Student_Record['English'][i]>50):
        print(f"{Student_Record['Stdname'][i]:<15} {Student_Record['Age'][i]}")

# Name and Age of Top 4 students with maximum marks in Maths
sorted_indices = sorted(range(len(Student_Record['Maths'])), key=lambda i: Student_Record['Maths'][i], reverse=True)
print("\nTop 4 students with highest marks in maths:")
print("S No.  Name            Age")
for i in range(4):
    idx = sorted_indices[i]
    print(f"{i+1:<6} {Student_Record['Stdname'][idx]:<15} {Student_Record['Age'][idx]}")
    
# srudent_id, Name and Age of Lowest 3 students with minimum marks in Computer
sorted_cs = sorted(range(len(Student_Record['Computer'])), key=lambda i: Student_Record['Computer'][i])
print("\nLowest 3 students with minimum marks in computer:")
print("S No.  ID       Name            Age")
for i in range(3):
    idx = sorted_cs[i]
    print(f"{i+1:<6} {Student_Record['Stdid'][idx]:<8} {Student_Record['Stdname'][idx]:<15} {Student_Record['Age'][idx]}")