#1
import functions_exercises as f
f.cumsum([1,2,3])

from functions_exercises import get_letter_grade
get_letter_grade

from functions_exercises import handle_commas as git_rid_of_commas
git_rid_of_commas('1,675,342,324')

#itertools
import itertools

#1 
for product in itertools.product('abc','123'):
    x = product.count('1')
    print(x)

for comb in itertools.combinations('abcd', 2):
    print comb

import json.load(open("profiles.json"))
data_table = json.load(open("profiles.json"))    
len(data_table)
active_users = [d for d in data_table if d['isActive'] == True]
len(active_users)
inactive_users = [d for d in data_table if d['isActive'] == False]
len(inactive_users) 
balances = [d['balance'] for d in data_table]
for b in balances:
    [b.replace("$", "") for b in balances]
    [b.replace(",", "") for b in balances]
    [float(b) for b in balances]

new_balances = [float(b.replace("$", "").replace(",","")) for b in balances]
sum(new_balances)
len(new_balances)
sum(new_balances)/len(new_balances)   
fix = float(d['balance'].replace("$", "").replace(",","")) for d in data_table
user_balance = [(d['name'], float(d['balance'].replace("$", "").replace(",",""))) for d in data_table]
float(d['balance'].replace("$", "").replace(",","")).min()
min(user_balance, key = lambda item: item[1])
max(user_balance), key = lambda item: item[1])

fruits = [d['favoriteFruit'] for d in data_table] 
fruit_set = set(fruits)
list(fruit_set)

def fruit_count(string):
    x = 0
    for fruit in fruits:
        if fruit == string:
            x += 1
    return x
fruit_count('banana')
fruit_count('apple')
fruit_count('strawberry')

def fruit_set_count():
    x = 0
    y = 0
    z = 0
    for fruit in fruits:
        if fruit == 'banana':
            x += 1
        if fruit == 'apple':
            y += 1
        if fruit == 'strawberry':
            z += 1
    return f'Banana Count = {x}, Apple Count = {y}, Strawberry Count = {z}'

max(fruits)
min(fruits)
def unread_messages():
    greetings = [d['greeting'] for d in data_table]
    cleaned = [g[g.index('have ')+5:].replace(" unread messages.","") for g in greetings]
    int_cleaned = [int(c) for c in cleaned]
    return sum(int_cleaned)