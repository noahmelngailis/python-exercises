#1a
day_of_week = input("Please enter day of the week ")
if day_of_week.capitalize() == "Monday":
    print("It's Monday!!!!")
else:
    print(f"{day_of_week} is not Monday")

#1b
weekend_day = input('Please enter day of the week ')
if (weekend_day.capitalize() == "Saturday" or 
    weekend_day.capitalize() == "Sunday"):
    print(f"{weekend_day.capitalize()} is a weekend day")
else:
    print(f"Get back to work, it's only {weekend_day.capitalize()}")

weekend_day = input('Please enter day of the week ')
if weekend_day.capitalize() in ["Saturday" "Sunday"]:
    print(f"{weekend_day.capitalize()} is a weekend day")
else:
    print(f"Get back to work, it's only {weekend_day.capitalize()}")

#1c
work_hours = input("How many hours did you work this week?")
hourly_rate = 25
work_hours = int(work_hours)
if work_hours <= 40:
    paycheck = work_hours * hourly_rate
    print(paycheck)
else:
    paycheck = 40 * hourly_rate + (work_hours - 40) * 1.5 * hourly_rate
    print(paycheck)




#2a
i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print(i)
    if i < 100:
        i += 2
    else:
        i
        break

while i >= -10:
    print(i)
    i -= 5

i = 2
while i <= 1000000:
    print(i) 
    i**=2

i = 100
while i > 0:
    print(i)
    i -= 5

#2bi
number = [n*7 for n in range(1,11)]

for n in range(1,11):
    print(n*7)

number = int(input("Please enter an integer"))
i = 1
while i <= 10:
    print(f"{number} x {1} = {number * i}")
    i += 1

#2bii
for n in range(1,10):
    print(str(n) * n)

#2ci
prompt = input("Pick an odd number between 1 and 50")
prompt = int(prompt)
i = 1
if prompt % 2 == 1 and prompt < 50 and prompt > 0:
    while i < prompt:
        print(f'Here is an odd number {str(i)}')
        i += 2
    print(f'Yikes! Skipping number: {str(prompt)}')
    i += 2
    while i < 50:
        print(f'Here is an odd number {str(i)}')
        i += 2
else:
    print("No good")
    prompt = input("Pick an odd number between 1 and 50")    

user_choice = input("Input an odd integer between 1 and 50")
while (user_choice.isdigit() == False
    or int(user_choice) < 0
    or int(user_choice) > 50
    or int(user_choice % 2 == 0)):
    print(f"{user_choice} is nice, but we'll need an odd number between 1 and 50.")
    user_choice = input("Input an odd integer between 1 and 50")  
user_choice = int(user_choice)
for i in range(1, 50):
    if i % 2 == 0:
        continue
    if i == user_choice:
        print(f"skipping {i}")
        continue

    print(f"{i} is an odd number")


#2d
prompt2 = input("Enter a natural number ")
prompt2 = int(prompt2)
i = 0
while i <= prompt2:
    print(i)
    i += 1
prompt4 = input("Enter a natural number ")
prompt4 = int(prompt4)
for i in range(0,prompt4+1):
    print(i)

#2e
prompt3 = input("Enter a natural number ")
prompt3 = int(prompt3)
while  prompt3 > 0:
    print(prompt3)
    prompt3 -= 1

prompt5 = input("Enter a natural number ")
prompt5 = int(prompt5)
for i in range(1,prompt5+1):
    print(prompt5)
    prompt5 -= 1

#3 FizzBuzz
i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    else:
        print(i)
    i += 1



for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
#4
question = 'yes'
while question.lower() == 'yes':
    prompt6 = input("Enter an integer")
    prompt6 = int(prompt6)
    print("number|squared|cubed")
    for i in range(1, prompt6+1):
        print(str(i) + "  |  " + str(i**2) + "  |  " + str(i**3))
    question = input('Would you like to continue? ')



#5
grade = input("Supply a numerical grade from 0-100 ")
grade = int(grade)
if grade >= 88:
    print("A")
elif grade >= 80:
    print("B") 
elif grade >= 67:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")   
question = input("Would you like to continue?")
while question.lower() == 'yes':
    grade = input("Supply a numerical grade from 0-100 ")
    grade = int(grade)
    if grade >= 88:
        print("A")
    elif grade >= 80:
        print("B") 
    elif grade >= 67:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")   
    question = input("Would you like to continue?")

question = 'yes'
while question.lower() == 'yes':
    grade = input("Supply a numerical grade from 0-100 ")
    grade = int(grade)
    if grade >= 88:
        print("A")
    elif grade >= 80:
        print("B") 
    elif grade >= 67:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")   
    question = input("Would you like to continue?")   

books = [
    {
        "title": "Red Harvest",
        "author": "Dashiell Hammett",
        "genre": "Noir"
    },
    {
        "title": "The Long Goodbye",
        "author": "Philip Marlowe",
        "genre": "Noir"
    },
    {
        "title": "Curtain",
        "author": "Agatha Christie",
        "genre": "Mystery"
    },
    {
        "title": "The Hardly Boys",
        "author": "Yvonne King",
        "genre": "Mystery"
    },
    {
        "title": "Who Stole My Shoe",
        "author": "Ryan McCall",
        "genre": "Mystery"
    },
    {
        "title": "How I Learned to Love Roof Rabbits",
        "author": "Shay Altshue",
        "genre": "How to"
    },
    {
        "title": "Stuck in an Elevator: My First Day at CodeUp",
        "author": "Ryan McCall",
        "genre": "How to"
    }
]

for book in books:
    print(book['title'] +", by " + book['author'] + ", in genre: " + book['genre'])

call = input('Pick a genre: "Noir" "Mystery" or "How to"')
for book in books:
    if call.lower() == book['genre'].lower():
        print(book['title'] + " by " + book['author'])

