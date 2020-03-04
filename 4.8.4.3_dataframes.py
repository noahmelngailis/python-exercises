from pydataset import data

import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)

#1a
df['passing_english'] = df.english > 70  

#1b
df.sort_values('passing_english')
#1c
df.sort_values(['passing_english', 'name'])
#1d
df.sort_values(['passing_english', 'english'])
#1e 

df['overall_grade'] = (df.english + df.reading + df.math)/3

#2
mpg = data('mpg')
#[234 rows x 11 columns]
mpg.info()
mpg.describe()

mpg = mpg.rename(columns={'cty': 'city'}).rename(columns={'hwy': 'highway'})
mpg.rename(columns={'hwy': 'highway'})

mpg[mpg.city - mpg.highway > 0]

mpg['mileage_difference'] = mpg.highway - mpg.city

mpg.sort_values('mileage_difference', ascending = False)
mpg[mpg.mileage_difference == mpg.mileage_difference.max()]

mpg[mpg['class'] == 'compact'].sort_values('highway', ascending = False).head(1)
mpg[mpg['class'] == 'compact'].sort_values('highway', ascending = False).tail(1)

mpg['avg_mileage'] = (mpg.city + mpg.highway)/2

mpg[mpg['manufacturer']== 'dodge']