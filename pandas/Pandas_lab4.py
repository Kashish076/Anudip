# ILT8
# 1. Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.

import pandas as pd

file = pd.read_csv('lab.csv')
df = pd.DataFrame(file)
piv_tab = pd.pivot_table(df,
                             values = ['Sales Amount'],
                             index = ['Region','Manager','SalesMan'],
                             aggfunc={'Sales Amount':'sum'})
print(piv_tab)

# 2. Write a Pandas program to create a Pivot table and find the item wise unit sold.
import pandas as pd

file = pd.read_csv('lab.csv')
df = pd.DataFrame(file)
piv_tab = pd.pivot_table(df, values='Sales Amount', index='Item', columns='Region', aggfunc='sum', fill_value=0)
grouped  = df.groupby('Item')['Units'].sum().reset_index()
print(grouped)

# 3. Write a Pandas program to create a Pivot table and find the region wise, item wise unit sold.
import pandas as pd
df = pd.read_csv('lab.csv')
piv_tab = pd.pivot_table(df, values='Units', index=['Region', 'Item'], aggfunc='sum', fill_value=0)
print("Region, Item-wise Units Sold:")
print(piv_tab)

# 4. Write a Pandas program to create a Pivot table and count the manager wise sale and mean value of sale amount.
import pandas as pd
df = pd.read_csv('lab.csv')
piv_tab = pd.pivot_table(df, values='Sales Amount', index='Manager', aggfunc='sum', fill_value=0)
grouped = df.groupby('Manager')['Sales Amount'].agg(['mean','count']).reset_index()
print(grouped)
