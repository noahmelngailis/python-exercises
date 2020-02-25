movies = [{'movie': 'Mermaid', 'days': 3, 'price': 3 },
            {'movie': 'Brother', 'days': 5, 'price': 3},
            {'movie': 'Hercules', 'days': 1, 'price': 3}
]

sum([mo['days'] * mo['price'] for mo in movies]  )

employers = [
    {'company': 'Google', 'hourly': 400, 'time':6},
    {'company': 'Facebook', 'hourly': 350, 'time':10},
    {'company': 'Amazon', 'hourly': 380, 'time': 4}
]
weekly = [work['hourly'] * work['time'] for work in employers]
sum(weekly)


# My attempt with libraries
# 
# students = [
#     {'class_full': True, 'no_schedule_conflict': True, 'enrolled' = True}
#     {'class_full': True, 'no_schedule_conflict': False, 'enrolled' = True}
#     {'class_full': False, 'no_schedule_conflict': False, 'enrolled' = True}
#     {'class_full': False, 'no_schedule_conflict': True, 'enrolled' = True}
#     ]

# [student for student in students if 'class_full' == True and 'no_schedule_conflict' == True]

class_has_room = True
schedule_works = True

student_can_be_enrolled = class_has_room and schedule_works



# def discount_offer(premium, not_expired, multiple):
#     if premium == True: 
#         return True
#     elif not_expired == True and multiple == True:
#         return True
#     else:
#         return False

bought_multiples = False
offer_valid = True
premium_member = True

offer_can_be_applied = offer_valid and (bought_multiples or premium_member)



login_creds = dict(username='codeup', password='notastrongpassword' )

len(login_creds['password']) >= 5  
len(login_creds['username']) <= 20

login_creds['username'] != login_creds['password']

not(login_creds['username'] == " *" or login_creds['password'] == " *")

