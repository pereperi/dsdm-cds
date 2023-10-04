# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country


def total_registered_cases(covid_register, country):
    country_cases = covid_register[country]
    ncases = sum(country_cases)
    return ncases


# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#

def total_registered_cases_per_country(covid_register):
    total_cases = {}
    for country in covid_register:
        total_cases[country] = sum(covid_register[country])
    return total_cases


# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(covid_register):
    total_cases = total_registered_cases_per_country(covid_register)
    max_country = max(total_cases, key=total_cases.get)
    return max_country
