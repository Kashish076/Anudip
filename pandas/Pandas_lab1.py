# ILT 5
# 1. Suppose you are a teacher, and you want to analyze the exam scores of your students in a particular subject. You have recorded the scores of your students for a recent exam, and you want to represent this data using a Pandas Series.
import pandas as pd
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]
data = pd.Series(exam_scores,index=students, name= "Exam Scores")
print(data)

# 2. Suppose you want to track and analyze your household expenses for a month.You have recorded the expenses for various categories, such as groceries, utilities, rent,  transportation, and entertainment. You can represent this expense data using a Pandas Series.
import pandas as pd
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]
Monthly_Expenses = pd.Series(expenses,index=categories, name= "Monthly Expenses (USD)")
print(Monthly_Expenses)

# 3.  Suppose you want to track and analyze the monthly energy consumption in your home. You have recorded the monthly energy usage for electricity and gas over a year, and you want to represent this data using Pandas Series.
import pandas as pd
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
electricity_usage = [350, 320, 310, 330, 340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]
Ele_use = pd.Series(electricity_usage, index=months,name="Electricity Usage (kWh)")
print("\nElectricity Usage:\n",Ele_use)
Gas_use = pd.Series(gas_usage, index=months,name="Gas Usage (therms)")
print("\nGas Usage:\n",Gas_use)

# 4. Suppose you are managing a website and want to analyze the monthly revenue generated from advertising. You have recorded the monthly revenue for the past year, and you want to represent this data using a Pandas Series.
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
revenue = [5000, 5200, 4800, 5400, 5600, 5800, 6100, 5900, 6200, 6500, 7000, 6900]
Month_Rev = pd.Series(revenue,index=months,name="Monthly Advertising Revenue")
print(Month_Rev)

# ChatGpt Exercise


# lab 2

# 1. Write a Pandas program to create a dataframe from a dictionary and display it.
import pandas as pd
score={'Math':[78,85,96,80,86],
       'English':[84,94,89,83,86],
       'Hindi':[86,97,96,72,83]
       }
df = pd.DataFrame(score)
print("\n",df)

# 2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine',
                      'James', 'Emily','Michael', 'Matthew', 'Laura', 'Kevin','Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5,
                       np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no',
                         'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
print("\n",df)

# 3. Write a Pandas program to get the first 3 rows of a given DataFrame.

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia','Dima','Katherine', 
                      'James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5,
                       np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],'qualify': ['yes','no','yes','no','no','yes',
                        'yes','no','no','yes']}
df = pd.DataFrame(exam_data)
print("\nFirst three rows of the data frame:\n",df.head(3))

# 4. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine',
                      'James', 'Emily','Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],'qualify': ['yes','no','yes','no','no','yes',
                        'yes','no','no','yes']}
df = pd.DataFrame(exam_data)
print("Original Data\n",df)
selected = ['name','score']
print("Select specific columns:\n",df[selected])

