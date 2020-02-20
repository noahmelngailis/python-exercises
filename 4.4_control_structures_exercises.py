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

#2bii
for n in range(1,10):
    print(str(n) * n)

#2ci
prompt = input("Pick an odd number between 1 and 50")
for prompt in range(1,50):
    if not(prompt % 2 == 1 and prompt < 50 and prompt > 0):
        break
    else:
        print(prompt)

#2d


