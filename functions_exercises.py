#1
def is_two(x):
    if x in [2, '2']:
        return True
    else:
        return False
def is_two(x):
    return x in [2, '2']
    

#2
def is_vowel(x):
    x = x.lower()
    return x in ['a', 'e', 'i', 'o', 'u']

def is_vowel2(x):
    x = x.lower()
    return x in 'aeiou' and len(x) == 1

def is_vowel3(x):
    vowels = 'aeiou'
    for vowel in vowels:
        if letter.lower() == vowel:
            return True
    return False

#3
def is_consonant(x):
    if is_vowel(x) == True:
        return False
    if len(x) != 1:
        return False
    else:
        return True

def is_consonant(x):
    return x in 'bcdfghjklmnpqrstvwxyz' and len(x)  == 1

def is_consonant(x):
    return len(x) == 1 and x.isalpha() and not is_vowel(x)

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
        letter = letter.lower()
        if is_vowel(letter) == True:
            words = words.replace(letter,"")   
        else:
            continue
    return(words)

def remove_vowels(string):
    string_without_vowels = ''
    for c in string:
        if not is_vowel(c):
            string_without_vowels += c
    return string_without_vowels

def remove_vowels(string):
    return "".join([c for c in string if not is_vowel])
       
#10
def normalize_name(string):
    string = string.lower()
    string = string.strip()
    for char in string:
        if char == " ":
            string = string.replace(char,"_")  
    return string

def remove_special_characters(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])

def normalize_name(string):
    with_out_special_characters = remove_special_chars(string)
    return with_out_special_chars.lower().strip().replace(" ", "")

#11
def cumsum(numbers):
    total = 0
    cumulative_sums = []
    for n in numbers:
        total += n
        cumulative_sums.append(total)
    return cumulative_sums
        
#def cumsum(numbers)
   # return [sum(numbers[:i + 1]) for i, _ in enumerate(numbers)]

#Bonus 1

# def twelveto24(string):
#     if (string[-2]) == "A"
#         string = string - string[-1] - string[-2]



# #12       
# def col_index(col_name)

