import pandas as pd
df = pd.read_csv('GoogleApps.csv')


#1 Display the minimum, average, and maximum 'Rating' of paid and free apps ('Type') and round to the nearest tenth.
print(round(df.groupby(by = 'Type')['Rating'].agg(['min', 'mean', 'max']), 1))


#2 Display the minimum, median, and maximum 'Price' of paid apps (Type == 'Paid') for # different target audiences ('Content Rating')
print(df[df['Type'] == 'Paid'].groupby(by = 'Content Rating')['Price'].agg(['min', 'median', 'max']))


#3 Group the data by 'Category' and target audience ('Content Rating') however you prefer
#calculate the maximum number of 'Reviews' for each group.
#Compare the results for the 'EDUCATION', 'FAMILY', and 'GAME' categories:
#In which age group did the 'EDUCATION' category app receive the most reviews? 'FAMILY'? 'GAME'?


#Tip: You can select multiple columns from DataFrame at once using the following syntax:
# df[[<column 1>, <column 2>, <column 3>]]
temp = df.pivot_table(index = 'Content Rating', columns = 'Category', values = 'Reviews', aggfunc = 'max')
print(temp[['EDUCATION', 'FAMILY', 'GAME']])


#4 Group the paid (Type == 'Paid') apps by 'Category' and target audience ('Content Rating')
#Calculate the average number of 'Reviews' for each group
#Please note that some cells in the resulting table have the value “NaN” – Not a Number – instead of a number
#That means that there are no apps in that group.
#Choose the names of the categories that have paid apps for all age groups and arrange them in alphabetical order.
print(df[df['Type'] == 'Paid'].pivot_table(columns = 'Content Rating', index = 'Category', values = 'Reviews', aggfunc = 'mean'))


#Bonus task. Find the categories of free (Type == 'Free') apps
#in which groups were the apps not designed for all age groups ('Content Rating')
print(df[df['Type'] == 'Free'].pivot_table(index = 'Category', columns = 'Content Rating', values = 'Reviews', aggfunc = 'mean'))
