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
[len(student['pets']) for student in students if len(student['pets']) >= 3]
# What is the average grade for students with 0 pets?
no_pets_grades = [student['grades'] for student in students if len(student['pets']) == 0]
avg_no_pets_grades = [sum(grades)/len(grades) for grades in no_pets_grades] 
sum(avg_no_pets_grades)/len(avg_no_pets_grades)
# What is the average grade for web development students? data science students?
def avg_grade(key, item):
    ind_avg = []
    for student in students:
        if key == item:
            ind_avg += [sum(student['grades'])/len(student['grades'])]
        else:
            continue
    group_avg = sum(ind_avg)/len(ind_avg)
    return group_avg

avg_grade('student["course"]', 'web development')
avg_grade("student['course']", 'data science') 

# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
dark_drinkers = [student['grades'] for student in students if student['coffee_preference'] == 'dark']
avg_for_dark = [sum(d)/len(d) for d in dark_drinkers]
avg_list_dark = []
for d in dark_drinkers:
    mean = sum(d)/len(d)
    avg_list_dark.append(mean)
max(avg_for_dark)
min(avg_for_dark)
# What is the average number of pets for medium coffee drinkers?
def avg_pets_medium():
    no_med_drinkers = len([student for student in students if student['coffee_preference'] == 'medium'])
    medium_drinkers = [student['pets'] for student in students if student['coffee_preference'] == 'medium']
    flat_med = sum(medium_drinkers,[])
    avg_pets = len(flat_med)/no_med_drinkers
    return avg_pets
# What is the most common type of pet for web development students?
def common_pets():
    web_dev = [student['pets'] for student in students if student['course'] == 'web development']
    flat_pets = sum(web_dev,[])
    horse = 0
    dog = 0
    cat = 0
    for l in flat_pets:
        if l['species'] == 'horse':
            horse +=1
        if l['species'] == 'dog':
            dog += 1
        if l['species'] == 'cat':
            cat += 1
    return f"Horse: {horse}, Dog: {dog}, Cat: {cat}"

web_dev = []
    for student in students:
        if student['course'] == 'web devolopment':
            pets += student['pets']
            web_dev.append(pets)
    return web_dev
# What is the average name length?
def avg_name_length():
    names = [len(student['student']) for student in students]
    avg_name_length = sum(names)/len(names)
    return avg_name_length

# What is the highest pet age for light coffee drinkers?

def highest_pet_age():
    pets = [student['pets'] for student in students if student['coffee_preference'] == 'light']
    flat_pets = sum(pets,[])
    max_age = max([p['age'] for p in flat_pets])
