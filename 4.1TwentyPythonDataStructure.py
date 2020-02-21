# How many students are there?
len(students)
# How many students prefer light coffee? For each type of coffee roast?
len([student for student in students if student['coffee_preference'] == 'light']) 
# How many types of each pet are there?
pets = [student['pets'] for student in students]
flattened_list = sum(pets,[])
len(set([flat['species'] for flat in flattened_list] ) )

species = []
for student in students:
    for pet in student['pets']:
        species.append(pet["species"])
len(set(species))

# How many grades does each student have? Do they all have the same number of grades?
grades = [len(student['grades']) for student in students]
set(grades)
# What is each student's grade average?
grades2 = [student['grades']) for student in students]
avg_grade = 
[student['student'] + "  :  " + str(sum(student['grades'])/len(student['grades'])) for student in students]

# How many pets does each student have?
[student['student'] + "  :  " + str(len(student['pets'])) for student in students]

# How many students are in web development? data science?
num_data_science = len([student['course'] for student in students if student['course'] == 'data science'])
num_web_dev = len([student['course'] for student in students if student['course'] == 'web development'])
# What is the average number of pets for students in web development?
flatten = sum([student['pets'] for student in students if student['course'] == 'web development'],[])
avg_pet_per_student = len(flatten)/len([student for student in students if student['course'] == 'web development'])
# What is the average pet age for students in data science?
data_sci = [student['pets'] for student in students if student['course'] == 'data science']
flatten_data_sci = sum(data_sci, [])
f_d_s = [flat['age'] for flat in flatten_data_sci]
sum(f_d_s)/len(f_d_s)
# What is most frequent coffee preference for data science students?
cof_dat = [student['coffee_preference'] for student in students if student['course'] == 'data science']
# What is the least frequent coffee preference for web development students?
# What is the average grade for students with at least 2 pets?
# How many students have 3 pets?
len([student for student in students if len(student['pets']) == 3])
# What is the average grade for students with 0 pets?
# What is the average grade for web development students? data science students?
# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# What is the average number of pets for medium coffee drinkers?
# What is the most common type of pet for web development students?
# What is the average name length?
# What is the highest pet age for light coffee drinkers?