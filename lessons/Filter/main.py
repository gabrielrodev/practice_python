# filter(function, collection) = return all elements that pass a condition

#def is_passing(grade):
#    return grade >= 60

grades = [70,92,81,32,52,84,27,39,59,69,10]

passing_grades = list(filter(lambda grade: grade >= 60, grades))

print(passing_grades)
#for grade in passing_grades:
#    print(grade)

#if its true you 