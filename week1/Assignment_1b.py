import pandas as pd

# student record
df = pd.DataFrame({
'stdid' : ['std101','std102','std103','std104','std105','std106','std107','std108','std109','std110'],
'stdname' : ['Ashish kumar','Abhishek kumar','Aman','Rahul','Ruby','Suamn','Saurabh','sumit','Kamlesh','Rohan'],
'standard' : ['10th','10th','10th','10th','10th','10th','10th','10th','10th','10th'],
'age' : [15,14,15,14,13,13,15,14,15,15],
'hindi' : [67,85,23,45,89,90,45,23,45,34],
'english' : [89,45,56,67,67,46,23,45,56,12],
'maths' : [87,48,78,45,89,67,34,67,78,24],
'science' : [89,90,78,45,93,67,45,78,99,45],
'computer' : [90,45,67,56,65,67,34,90,67,56]
})

#name and age of top 4 students in maths
top_4_maths = df.nlargest(4, 'maths')
print("Top 4 students with highest marks in maths:")
print("S No.  Name             Age")
for i, row in enumerate(top_4_maths.itertuples(), start=1):
    print(f"{i:<6} {row.stdname:<15} {row.age}")
      
print ("\n")

#name,id,age of students who are bottom 3 in computer
min_3_cs = df.nsmallest(3,'computer')
print("3 students with min marks in computer:")
print("Sno.   S_id.      Name           Age")
for i, row in enumerate(min_3_cs.itertuples(), start=1):
    print(f"{i:<6} {row.stdid:<10} {row.stdname:<15} {row.age}")

print("\n")