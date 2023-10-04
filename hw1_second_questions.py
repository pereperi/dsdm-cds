# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(cv_list, job_title):
    result_users = []
    for cv in cv_list:
        if job_title in cv['jobs']:
            result_users.append(cv['user'])
    return result_users

#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(cv_list):
    final_dict = {}
    for cv in cv_list:
        for job in cv['jobs']:
            if job in final_dict:
                final_dict[job] += 1
            else:
                final_dict[job] = 1
    return final_dict


#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.


def most_popular_job(cv_list):
    count_jobs = job_counts(cv_list)
    curr_max = 0
    first_tup = None
    for job in count_jobs.items():
        if job[1] > curr_max:
            first_tup = job
            curr_max = job[1]
    return first_tup

