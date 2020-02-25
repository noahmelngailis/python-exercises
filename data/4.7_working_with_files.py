# Read the contents of your last exercise file into a variable.
with open ("4.6_import_exercises.py") as f:
    file_contents = f.read()
# Print out every line in the file
with open ("4.6_import_exercises.py") as f:
    file_contents = f.read()
    print(file_contents)
# Print out every line in the file, but add a line numbers
with open ("4.6_import_exercises.py") as f:
    lines = f.readlines()
    line_number = list(enumerate(lines))    
    for i,x in line_number:
        print(i, x)                                                                                    
      
# Write some python code to create a grocery list.
# Create a variable named grocery_list. It should be a list, 
# and the elements in the list should be a least 3 
# things that you need to buy from the grocery store.
grocery_list = ['strawberries', 'steak', 'toilet paper']

# Create a function named make_grocery_list. When run, 
# this function should write the contents of the grocery_list
#  variable to a file named my_grocery_list.txt.
def make_grocery_list(x = grocery_list):
    with open('my_grocery_list.txt', 'a') as f:
        for i in x:
            f.writelines(i + " \n")

def make_grocery_list_too(x = grocery_list):
    filename = 'my_grocery_list2.txt'
    with open (filename, 'a') as f:
        for item in grocery_list:
            f.write(item + '\n')

# Create a function named show_grocery_list. 
# When run, it should read the items from the text file and
#  show each item on the grocery list.
def show_grocery_list():
    with open('my_grocery_list.txt', 'r') as f:
        lines = f.readlines()
        return lines

def show_grocery_list_too():
    with open('my_grocery_list2.txt') as f:
        contents = f.readlines()
        for item in contents:
            print(item)
# Create a function named buy_item. 
# It should accept the name of an item on the grocery list, 
# and remove that item from the list.
def buy_item(item_bought):
    make_grocery_list()
    with open('my_grocery_list.txt') as f:
        lines = f.readlines()
    with open('my_grocery_list.txt', 'w') as ff:
        for item in lines:
            if item.strip('\n') == item_bought:
                print(item)

def buy_item(item_bought):
    with open('my_grocery_list.txt') as f:
        items = f.readlines()
    with open('my_grocery_list.txt', 'w') as f:
        for item in items:
            if item.strip('\n') != item_bought:
                list_item = item
        f.write()
    with open('my_grocery_list.txt') as f:
         print(f.read())

def buy_item_too(item):
    grocery_list.remove(item)
    make_grocery_list(grocery_list)

