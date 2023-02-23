import pandas as pd
import plotly.express as px

df = pd.read_excel("Project_File.xlsx")
df.head()
print(df.shape)

print(df.shape)
df.astype("str")
df = df.rename(columns={df.columns[0]: "Year"})
df[['Year','Month']] = df['Year'].str.split(n = 1, expand=True)

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
# Removing all NA and replacing with 0
df = df.replace(' na ', 0)
# Converting all columns to integers
df = df.apply(pd.to_numeric)
df = df["1987"]





