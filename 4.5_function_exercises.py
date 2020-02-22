#1
def is_two(x):
    if x in [2, '2']:
        return True
    else:
        return False

#2
def is_vowel(x):
    if x in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

#3
def is_consonant(x):
    if is_vowel(x) == True:
        return False
    if len(x) != 1:
        return False
    else:
        return True

#4
def capitalize_word(word):
    y = word[0].lower()
    if is_vowel(y) == True:
        return word
    else:
        return word.capitalize()

#5
def calculate_tip(bill, tip_percent):
    tip = bill * tip_percent
    return tip

#6 
def apply_discount(original_price, discount_percentage):
    discount_amount = original_price * discount_percentage
    new_total = original_price - discount_amount
    return new_total
    
#7
def handle_commas(entry):
    entry = entry.replace(',', '')
    entry = int(entry)
    return entry

#8
def get_letter_grade():
    x = input("Enter a score:")
    while (x.isdigit() == False
        or int(x) > 100
        or int(x) < 0):
        x = input("Enter a score:")
    x = int(x)
    if x >= 90:
        x = "A"
        return f"You got an {x}"
    elif x >= 80:
        x = "B"
        return f"You got an {x}"
    elif x >= 70:
        x = "C"
        return f"You got an {x}"
    elif x >= 60:
        x = "D"
        return f"You got an {x}"
    else:
        x = "F"
        return f"You got an {x}"

#9
def remove_vowels(words):
    for letter in words:
        if is_vowel(letter) == True:
            
        else:
            print(letter)
       
        

def remove_vowels(words):
    is_vowel(letter)
    [letter.replace(y,"") for letter in words if is_vowel(letter) == True]
    return words 

#10