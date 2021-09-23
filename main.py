import random
import time
import os
import string

def clear():
    time.sleep(1)
    if os.name == 'nt':
        _ = os.system('cls')

def typing_tips():
    print("====================== WELCOME TO THE TYPEWRITER-TIPS ======================")
    print("1) First sit with comfarat and place your keyboard at right place.")
    print("2) Use your all fingers for typing with the thumb used for space bar.")
    print("3) Explore the keys on the keyboard with the use of the fingers.")
    print("4) Learn the new shortcut keys using the keyboard")
    print("5) Avoid to watch keyboard while typing and try keep your eyes on screen.")
    decision = input("[ If you want to go back yes/no :- y/n ]")
    if decision == "y":
        repeat()
    else:
        exit()
    
    

def typing_practice():
    print("Hello world")
    pass

def typing_test():
    print("Hello world")
    pass


def repeat():
    choice  = "" # initliazing variable
    
    clear()
    print("====================== WELCOME TO THE TYPEWRITER ======================")
    print("1) For typing tips")
    print("2) For Typing Practice")
    print("3) For typing Test")
    print("4) For Exit")
    choice = input()
    # End of while loop

    if choice == "1":
        clear()
        typing_tips() # going to typing tips

    if choice == "2":
        clear()
        typing_practice()# going to typing practice

    if choice == "3":
        clear()
        typing_test()# going to typing test

    if choice == "4":
        exit() # Exit

if __name__ == '__main__':
    choice  = "" # initliazing variable
    
    clear()
    print("====================== WELCOME TO THE TYPEWRITER ======================")
    print("1) For typing tips")
    print("2) For Typing Practice")
    print("3) For typing Test")
    print("4) For Exit")
    choice = input()
    # End of while loop

    if choice == "1":
        clear()
        typing_tips() # going to typing tips

    if choice == "2":
        clear()
        typing_practice()# going to typing practice

    if choice == "3":
        clear()
        typing_test()# going to typing test

    if choice == "4":
        exit() # Exit


        
