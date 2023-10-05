# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#

def triple(x):
    return 3*x

# Test of the "triple" function
test_values = [1, 2, 3, 4, 5]
results_triple = [triple(x) for x in test_values]

results_triple

# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(x,y):
    return y-x

# Test of the "subtract" function
test_values_x = [10, 20, 30, 40, 50]
test_values_y = [5, 10, 15, 20, 25]
results_subtract = [subtract(y, x) for y, x in zip(test_values_x, test_values_y)]

results_subtract


# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
# You should program the function and not use
# the function "dict" directly

def dictionary_maker(tuples_list):
    result_dict = {}
    for tup in tuples_list:
        key, value = tup
        result_dict[key] = value

    return result_dict

# Test of the "dictionary_maker" function
test_tuples = [('foo', 1), ('bar', 3)]
result_dictionary_maker = dictionary_maker(test_tuples)

result_dictionary_maker

