import pandas as pd
print(pd.__version__)
data = [10,20,30,40]
series = pd.Series(data)
header  = f"s.no. ser"
print(f"{header}\n{series}")
print(series[2])
print(type(series))

print("-----------------------------------------------------------------------")
months = ["january","February","March","April","May","June","July","August","September","October","November","December"]
Sales = [100,200,100,102,202,300,71,103,203,90,100,23]
series_sales = pd.Series(Sales,index = [months])
print(series_sales)

print("-----------------------------------------------------------------------")
data = {'Name':['Alice','bob','Charlie','David'],'Age': [25,30,24,28],'City': ['New York','Los Angeles', 'Chicago', 'Houston']}
df =pd.DataFrame(data)
print(df)

print("-----------------------------------------------------------------------")
data = {'Name':['Alice','bob','Charlie','David'],'Age': [25,30,24,28]}
df =pd.DataFrame(data)
print("Before adding column:\n",df)
df['City']= ['New York','Los Angeles', 'Chicago', 'Houston']
print("After adding column:\n",df)

print("-----------------------------------------------------------------------")
data = {'Name':['Alice','bob','Charlie','David'],'Age': [25,30,24,28],'City': ['New York','Los Angeles', 'Chicago', 'Houston']}
df =pd.DataFrame(data)
print(df)

new_columns ={'Gender' : ['Female','Male','Male','Male']
              ,'Grade' : ['A','B','B','A']}
df['Gender'] = new_columns['Gender']
df['Grade'] = new_columns['Grade']
print("\nDataFrame after adding new columns:\n",df)

print("-----------------------------------------------------------------------")
data = {'Name':['Alice','bob','Charlie','David'],'Age': [25,30,24,28],'City': ['New York','Los Angeles', 'Chicago', 'Houston']}
df =pd.DataFrame(data)
print("Before inserting \n",df)

df.insert(1,'Gender',['Female','Male','Male','Male'])
print("After inserting\n",df)

#To add new rows we use concat() function in pandas
print("-----------------------------------------------------------------------")
data = {'Name':['Alice','bob','Charlie','David'],'Age': [25,30,24,28],'City': ['New York','Los Angeles', 'Chicago', 'Houston']}
df =pd.DataFrame(data)
print("Before concatination:\n",df)
new_row = pd.DataFrame([{'Name' : 'Eve', 'Age': 24,'City':'San Francisco'}])
print(new_row)
df= pd.concat([df, new_row] , ignore_index=True)
print(df)

print("-----------------------------------------------------------------------")
data = {'Name':['Alice','bob','Charlie','David'],'Age': [25,30,24,28],'City': ['New York','Los Angeles', 'Chicago', 'Houston']}
df =pd.DataFrame(data)
print("Initial DataFrame:")
print(df)
new_rows = pd.DataFrame([{'Name' : 'Eve', 'Age': 24,'City':'San Francisco'},{'Name' : 'Frank', 'Age': 32,'City':'Miami'},{'Name' : 'Grace', 'Age': 29,'City':'Seattle'}])
new_df = pd.concat([df,new_rows], ignore_index=True)
print(new_df)

# Loc()
print("-----------------------------------------------------------------------")
data = {'Name':['Alice','bob','Charlie','David'],'Age': [25,30,24,28],'City': ['New York','Los Angeles', 'Chicago', 'Houston']}
df =pd.DataFrame(data)
print("Initial data:")
print(df)

row2 = {'Name' : 'Eve', 'Age': 24,'City':'San Francisco'}
df.loc[3]= row2
df = df.rename(columns={'Name' : 'First Name' })
print("Data after updation:")
print(df)

# colors
print("-----------------------------------------------------------------------")
fruit_data = {'Name':['Apple','Avacado','Banana','Strawberry','Grape'],'color':['Red','Green','Yellow','Pink','Green'],'Price':[45,90,65,37,49]}

data = pd.DataFrame(fruit_data)
print("Original Dataset")
print(data)

data['Price']
data.loc[data['Price']>60,'Remarks'] = 'Expensive'
data.loc[data['Price']<60,'Remarks'] = 'Not Expensive'
print("After Updating Values:")
print(data)

# deletion
print("-----------------------------------------------------------------------")
data = {'emp id':[101,102,103,104,105],
        'Name': ['Alice','Bob','Charlie','David','Eve'],
        'Age':[8,27,25,30,29]}
df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)

employ_del = 'Alice'
df = df.loc[df['Name']!='Alice']
print("Data after deletion:")
print(df)

# pop()
print("-----------------------------------------------------------------------")
data = {'emp id':[101,102,103,104,105],
        'Name': ['Alice','Bob','Charlie','David','Eve'],
        'Age':[8,27,25,30,29]}
df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)

df.pop('Age')
print("Data after popping of age column")
print(df)

# del()
print("-----------------------------------------------------------------------")
data = {'emp id':[101,102,103,104,105],
        'Name': ['Alice','Bob','Charlie','David','Eve'],
        'Age':[8,27,25,30,29]}
df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)

del df['Name']
print("Data after deletion of Names:")
print(df)

# Arithmetic operations
print("-----------------------------------------------------------------------")
dict = {'a':[1,2,3,4,5],'b':[2,4,6,8,1]}
df = pd.DataFrame(dict)
print("Initial Data:")
print(df)
df['sum'] = df['a'] + df['b']
df['sub'] = df['a'] - df['b']
df['product'] = df['a'] * df['b']
print("Data after arithmetic operations:")
print(df)

# iloc[] function
print("-----------------------------------------------------------------------")
data = {'Name':['Alice','bob','Charlie','David'],'Age': [25,30,24,28],'City': ['New York','Los Angeles', 'Chicago', 'Houston']}
df =pd.DataFrame(data)
print("Initial DataFrame:")
print(df)
new_rows = pd.DataFrame([{'Name' : 'Eve', 'Age': 24,'City':'San Francisco'},{'Name' : 'Frank', 'Age': 32,'City':'Miami'},{'Name' : 'Grace', 'Age': 29,'City':'Seattle'}])
df = pd.concat([df.iloc[:1],new_rows, df.iloc[1:]]).reset_index(drop=True)

print("updated data:")
print(df)

print("-----------------------------------------------------------------------")
import pandas as pd
file = 'dataset.csv'
cols = ['Name','Age','Gender','Marital Status','City','Salary','Payment Method','Amount Spent']
df = pd.read_csv(file,usecols=cols)
female_person = df['Gender'] == 'Female'
married_person = df['Marital Status'] == 'Married'
loc_newyork = df['City'] == 'New York'
print(df[female_person&married_person&loc_newyork].head(4))

print("-----------------------------------------------------------------------")
import pandas as pd
file = 'dataset.csv'
df = pd.read_csv(file)
print(df[['Salary']].groupby(df['Gender']).max())

print("-----------------------------------------------------------------------")
