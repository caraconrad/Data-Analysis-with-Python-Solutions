import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex']=='Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percent_education = df['education'].value_counts(normalize=True).mul(100).round(1)    
    percentage_bachelors = percent_education['Bachelors']

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    degrees = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df.education.isin(degrees)]
    lower_education = df[~df.education.isin(degrees)]    

    # percentage with salary >50K
    higher_percent_salary = higher_education['salary'].value_counts(normalize=True).mul(100).round(1)
    lower_percent_salary = lower_education['salary'].value_counts(normalize=True).mul(100).round(1)

    higher_education_rich = higher_percent_salary['>50K']
    lower_education_rich = lower_percent_salary['>50K']

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week']==1]

    rich_percentage = num_min_workers['salary'].value_counts(normalize=True).mul(100).round(1)['>50K']

    # What country has the highest percentage of people that earn >50K?
    unique_countries = df['native-country'].unique().tolist()
    countries_dict = {elem : pd.DataFrame for elem in unique_countries}
    
    for key in countries_dict.keys():
        countries_dict[key] = df[:][df['native-country'] == key]

    country_rich_percent = {}
   
    for country in unique_countries:        
        if country != '?':            
            try:
                country_rich_percent[country] = countries_dict[country]['salary'].value_counts(normalize=True).mul(100).round(1)['>50K']
            except:
                country_rich_percent[country] = 0.0    

    highest_earning_country = max(country_rich_percent, key=country_rich_percent.get)
    highest_earning_country_percentage = max(country_rich_percent.values())

    # Identify the most popular occupation for those who earn >50K in India.
    rich_india = countries_dict['India'][countries_dict['India']['salary']=='>50K']
    top_IN_occupation = rich_india['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
