import pandas as pd
df = pd.read_csv('GoogleApps.csv')


#1 How many apps are there in the 'BUSINESS' 'Category'?
print(df['Category'].value_counts())


#2 What is the ratio of apps for teenagers ('Teen') to those for children over 10 years old ('Everyone 10+')?
#Round the answer to the nearest hundredth.
temp = df['Content Rating'].value_counts()
print('Ratio:', round(temp['Teen'] / temp['Everyone 10+'], 2))


#3.1 What is the average 'Rating' of 'Paid' apps?
#Round the answer to the nearest hundredth.
temp = df.groupby(by = 'Type')['Rating'].mean()
print(temp['Paid'])


#3.2 How much lower is the average 'Rating' of 'Free' apps than the average rating of 'Paid' apps?
#Round the answer to the nearest hundredth.
print(round(temp['Paid'] - temp['Free'], 2))


#4 What are the minimum and maximum app 'Size' in the 'COMICS' 'Category'?
#Round the answer to the nearest hundredth.
print(df.groupby(by = 'Category')['Size'].agg(['min', 'max']))


#Bonus 1. How many apps have a 'Rating' of over 4.5 in the 'FINANCE' 'Category'?
temp = df[df['Rating'] > 4.5]['Category'].value_counts()
print(temp['FINANCE'])


#Bonus 2. What is the ratio of 'Free' to 'Paid' games with a 'Rating' greater than 4.9?
temp = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(temp['Free'] / temp['Paid'])