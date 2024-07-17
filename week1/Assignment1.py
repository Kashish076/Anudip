# student record
stdid = ['std101','std102','std103','std104','std105','std106','std107','std108','std109','std110']
stdname = ['Ashish kumar','Abhishek kumar','Aman','Rahul','Ruby','Suamn','Saurabh','sumit','Kamlesh','Rohan']
standard = ['10th','10th','10th','10th','10th','10th','10th','10th','10th','10th']
age = [15,14,15,14,13,13,15,14,15,15]
hindi = [67,85,23,45,89,90,45,23,45,34]
english = [89,45,56,67,67,46,23,45,56,12]
maths = [87,48,78,45,89,67,34,67,78,24]
science = [89,90,78,45,93,67,45,78,99,45]
computer = [90,45,67,56,65,67,34,90,67,56]

Student_Record = [stdid, stdname, standard, age, hindi, english, maths, science, computer]
print("Student Records:")
for i in range(len(stdid)):
    print(Student_Record[0][i], Student_Record[1][i], Student_Record[2][i], Student_Record[3][i], Student_Record[4][i],Student_Record[5][i],Student_Record[6][i],Student_Record[7][i],)
print("---------------------------------------------------------")
print("Students with more than 50 m arks in english: ")
for i in range (10):
    if(english[i]>50):
        print(stdname[i])
print("---------------------------------------------------------")
