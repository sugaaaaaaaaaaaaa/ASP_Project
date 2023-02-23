import pandas as pd
import plotly.express as px
import unittest
import numpy as np
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_excel("Project_File.xlsx")
df.head()
print(df.shape)

# Change all to string
df.astype("str")

# Split Year and Month
df = df.rename(columns={df.columns[0]: "Year"})
df[['Year','Month']] = df['Year'].str.split(n = 1, expand=True)

# Removal of White space
df.columns = df.columns.str.strip()
print(df.columns)

# Choose Asia as the region
df = df[['Year','Brunei Darussalam', 'Indonesia', 'Malaysia', 'Philippines', 'Thailand',
      'Viet Nam', 'Myanmar', 'Japan', 'Hong Kong', 'China', 'Taiwan',
       'Korea, Republic Of', 'India', 'Pakistan', 'Sri Lanka', 'Saudi Arabia',
       'Kuwait', 'UAE']]
print(df)

print(df.shape)
print(df)

# Filtering of Year
df = df[(df['Year'] > "1978") & (df['Year'] < "1988")]
print(df)
year = df[(df['Year'] > "1978") & (df['Year'] < "1988")]
# Removing all NA and replacing with 0
df = df.replace(' na ', 0)
print(df)
# Converting all columns to integers
df = df.apply(pd.to_numeric)
print(df.info())
print(df.isna().sum())
print(df.info())

# Plotting of Graph
# fig = px.bar(df, x=df['Year'], y=df.columns)
# fig.show()
# matplotlib test



#fig = plt.figure(facecolor =  'white', figsize = (10, 10))
#ax = plt.axes()
#ax.bar(Year - 0.25, data[0], color = 'red', width = 0.25)
#ax.bar(Year + 0.0, data[1], color = 'green', width = 0.25)
#ax.bar(Year + 0.25, data[2], color = 'blue', width = 0.25)



# Top 3 countries in selected 10 years
#print((df.sum(axis=0).sort_values(ascending= False)))




grouped_by_test = df.groupby('Year').sum()   ##Fking finally i swear this took way too fking long to figure out
print(grouped_by_test)


#fig = plt.figure(facecolor =  'white', figsize = (10, 10))
#ax = plt.axes()
#ax.bar()
#ax.legend(labels=[])
#plt.title("Visitors", size = 18)
#plt.xlabel("Years", size = 12)
#plt.ylabel("Number of Visitors", size = 12)
#plt.xticks(year)
#plt.show()


#ps=grouped_by_test
#index= np.arange(len(ps.index))
#plt.xlabel("Years", size = 5)
#plt.ylabel("Number of Visitors", size = 10)
#plt.xticks(index,ps.index,fontsize=10, rotation=90)
#plt.title("Visitors per Year")
#plt.bar(grouped_by_test,height=grouped_by_test)
#plt.savefig("testname.png")



ax= grouped_by_test.plot(kind='bar',title='visitors per year',figsize=(6,6),legend=True,fontsize=12,style=dict )
plt.show()

grouped_by_test.plot()


#import unittest

#class DA(unittest.TestCase):

       #def test_upper       (self):
              #self.assertEqual('foo'.upper(), 'FOO')

       #def test_isupper(self):
              #self.assertTrue('FOO'.isupper())
              #self.assertFalse('Foo'.isupper())

#if __name__=='__main__':
       #unittest.main()

