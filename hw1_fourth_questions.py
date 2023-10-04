# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #

import pandas as pd

covid = pd.read_csv("covid.csv")

def covid_summary(df, thresh):
    df1 = df[df['Active'] > thresh]
    print(df1['Country'])
    avg_deaths = df1['Deaths'].mean()
    avg_confirmed = df1['Confirmed'].mean()
    print("Average number of deaths: ", avg_deaths)
    print("Average number of confirmed cases: ", avg_confirmed)


covid_summary(covid, 500)
covid_summary(covid, 1000)
covid_summary(covid, 5000)