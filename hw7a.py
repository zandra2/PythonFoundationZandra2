''' Assignment

This assignment will include the following:

    Finish walking through this lecture to copy/paste the beginning of the script you will need for your homework.
        (Links to an external site.)Links to an external site.
    Finish the user option to delete an entry from the dictionary by removing the "pass" statements and adding
        code to delete a user by name (extra challenge: can you figure out how to delete a user by name OR username?)
    Finish the user option to lookup a username by name by removing the "pass" statement and adding code to find
        a user by name
    Run the script and make sure each option works
    Add exception handling to each user input option.
    Add doc strings to the script and comment the code.
    Push your finished script to your personal, publicly accessible Github repo.
    Submit a link to the Github repo containing your script on canvas.


Criteria
This criterion is linked to a Learning Outcome User can delete an entry from the dictionary. 25pts

This criterion is linked to a Learning Outcome User can lookup a username by name. 25pts

This criterion is linked to a Learning Outcome Each user option has exception handling. 25pts

This criterion is linked to a Learning Outcome Script contains helpful doc strings and comments 10pts

This criterion is linked to a Learning Outcome Finished script successfully uploaded to Github 25pts

'''

from sortedcontainers import SortedDict
import sys

#adding a comment here
#This is a public script using sortedcontainers.
#A dictionary is created which allows for user input to print/add/remove/lookup users

#!usr/bin/env python3

def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Username')
    print('5. Quit')
    print()


# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
# if an invalid menu choice is added, exception handling will
   #notify user that that only numbers are acceptable for options
while menu_choice != 5:

    # exception handling
    try:  # get menu choice from user
        menu_choice = int(input("Type in a number (1-5): "))
    except ValueError:
        print("Numbers Only")
        sys.exit()
    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username

    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        if name in usernames:
            usernames.pop(name) # delete that entry

    # view user name
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            print("The username is: {}".format(usernames[name])) # print the username
        else:
            print("username not found")  # print username not found

    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()