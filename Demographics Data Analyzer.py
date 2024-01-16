import pandas as pd
data = pd.read_csv('C:\\Users\\TOW Admin\\Downloads\\US Census\\adult.csv')
data.head()
race_counts = data['race'].value_counts()
average_age_men = round(data[data['sex'] == 'Male']['age'].mean(), 1)
percentage_bachelors = round((data['education'] == 'Bachelors').mean() * 100, 1)
higher_education = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
min_work_hours = data[' hours-per-week'].min()
num_min_workers = data[data[' hours-per-week'] == min_work_hours]
rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)
earning_above_50k = data[data['salary'] == '>50K']
country_stats = earning_above_50k['native-country'].value_counts() / data['native-country'].value_counts()
highest_earning_country = round((country_stats * 100).idxmax(), 1)
highest_earning_country_percentage = round((country_stats * 100).max(), 1)
india_high_earning = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
if india_high_earning.empty:
    top_IN_occupation = 'No occupation found'
else:
    top_IN_occupation = india_high_earning['occupation'].value_counts().idxmax()

top_IN_occupation