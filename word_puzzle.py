# Take the word EASY: Its first three letters — E, A and S — are the fifth,
#  first, and nineteenth letters, respectively, in the alphabet. If you add 5,
#  1, and 19, you get 25, which is the value of the alphabetical position of Y,
#  the last letter of EASY.

# Can you think of a common five-letter word
#  that works in the opposite way — in which the value of the alphabetical
#  positions of its last four letters add up to the value of the alphabetical
#  position of its first letter?


with open('/usr/share/dict/words') as f:
    words = f.read().split('\n')

list1 = list('abcdefghijklmnopqrstuvwxyz')
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
]

df = pd.DataFrame(list1)
df['num_value'] = list2
df['letters'] = list1

new_words = []
for w in words:
    if len(w) == 5:
        new_words.append(w)




for w in new_words:
    w = w.lower()
    list_word = list(w)
    for l in list_word:
        x == df.num_value.apply(lambda n: n if df.letters = 'a')
        
        
        if sum(list_word[0:3]) == list_word[4]:
            print(w)

def num_let(a)
    for a in df.letters
df.num_value.apply(lambda x: x if df.letters == True else False)
def num_let(a):
    if a == df.letters:
        return df.num_value


#Solution
 
 import pandas as pd

 with open('/usr/share/dict/words') as f:
    words = f.read().split('\n')

df = pd.DataFrame({'words': words})
df['word_length'] = df.words.apply(len)

five_letter_words = df[df.word_length == 5]

def alphabetical_value(ch: str) -> int:
    return 'abcdefghijklmnopqrstuvwxyz'.index(ch.lower())+1

alphabetical_value('f')

def test_word(word):
    first_letter, *last_four = word
    # first = word[0]
    # last = word[1:]
    return alphabetical_value(first_letter) == sum([alphabetical_value(ch) for ch in last_four])

mask = five_letter_words.words.apply(test_word)
five_letter_words[mask]

[word for word in words if len(word) == 5 and test_word(word)]
