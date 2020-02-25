# How many students are there?
len(students)
# How many students prefer light coffee? 
len([s for s in students if s['coffee_preference'] == 'light'])
#For each type of coffee roast?
def coffee_type():
    coffee_set = [s['coffee_preference'] for s in students]
    x = 0
    y = 0
    z = 0
    for c in coffee_set:
        if c == 'light':
            x += 1
        if c == 'medium':
            y += 1
        if c == 'dark':
            z += 1
    return f"light = {x}, medium = {y}, dark = {z}"
# How many types of each pet are there?
flatten_pets= sum([s['pets'] for s in students],[])
set([pet['species'] for pet in flatten_pets])
len(set([pet['species'] for pet in flatten_pets]))
# How many grades does each student have? Do they all have the same number of grades?
[len(s['grades']) for s in students]
# What is each student's grade average?
grades = [s['grades'] for s in students]
[sum(g)/len(g) for g in grades]
[(s['student'], sum(s['grades'])/len(s['grades'])) for s in students]
# How many pets does each student have?
[(s['student'], len(s['pets'])) for s in students]
# How many students are in web development? data science?

def what_class():
    course = [s['course'] for s in students]
    x = 0
    y = 0
    for c in course:
        if c == 'web development':
            x += 1
        if c == 'data science':
            y += 1
    return f"web development has {x} students and data science has {y} students"
# What is the average number of pets for students in web development?
 avg_web_pets = [(len(s['pets'])) for s in students if s['course'] == 'web development']
 sum(avg_web_pets)/len(avg_web_pets)
# What is the average pet age for students in data science?
avg_data_pets = [(len(s['pets'])) for s in students if s['course'] == 'data science']
sum(avg_data_pets)/len(avg_data_pets)
# What is most frequent coffee preference for data science students?
max([s['coffee_preference'] for s in students if s['course'] == 'data science'])
def coffee_type_data():
    coffee_set = [s['coffee_preference'] for s in students if s['course'] == 'data science']
    x = 0
    y = 0
    z = 0
    for c in coffee_set:
        if c == 'light':
            x += 1
        if c == 'medium':
            y += 1
        if c == 'dark':
            z += 1
    return f"light = {x}, medium = {y}, dark = {z}"
# What is the least frequent coffee preference for web development students?
min([s['coffee_preference'] for s in students if s['course'] == 'web development'])
# What is the average grade for students with at least 2 pets?
avg_grade_2_pets = [sum(s['grades'])/len(s['grades']) for s in students if len(s['pets']) >= 2]
sum(avg_grade_2_pets)/len(avg_grade_2_pets)
# How many students have 3 pets?

# What is the average grade for students with 0 pets?
# What is the average grade for web development students? data science students?
# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# What is the average number of pets for medium coffee drinkers?
# What is the most common type of pet for web development students?
# What is the average name length?
# What is the highest pet age for light coffee drinkers?