# Lambda function = A small anonymous function for a one time use (throw away function)
#                   They take any number of arguments, but have only 1 expression Helps keep the namespace clean
#                   and is useful with higher order functions
#                   'sort()', 'map()', 'filter()', 'reduce()'
#                   lambda parameters: expression

# EXAMPLE: map(lambda x: x * 2, numbers)

double = lambda x: x * 2 # x: accepts x
add = lambda x, y: x + y
max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y
full_name = lambda first, last: first + " " +last
is_even = lambda x: x % 2 == 0
age_check = lambda age: True if age >= 18 else False


print(age_check(20))