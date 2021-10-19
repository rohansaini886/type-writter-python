import random
import time
import os
import string

def clear():
    time.sleep(0.25)
    if os.name == 'nt':
        _ = os.system('cls')

def typing_tips():
    clear()
    print("====================== WELCOME TO THE TYPEWRITER-TIPS ======================")
    print("1) First sit with comfarat and place your keyboard at right place.")
    print("2) Use your all fingers for typing with the thumb used for space bar.")
    print("3) Explore the keys on the keyboard with the use of the fingers.")
    print("4) Learn the new shortcut keys using the keyboard")
    print("5) Avoid to watch keyboard while typing and try keep your eyes on screen.")
    decision = input("[ If you want to go back yes/no :- Y/n ]")
    if decision == "Y":
        repeat()
    else:
        exit()
    
def typing_practice():
    decision = input("[Want to try :- 'Y/n' ] ")

    if decision == "Y":
        file = open('paragraph.txt', 'r')
        Lines = file.readlines()
        st = random.choice(Lines)
        if st[-1] !=".":
            st += "."

        print(st)
        word_count = 0
        l = []
        word = ""
        for i in st:
            if i == " " or i == ".":
                l.append(word)
                word = ""
                word_count += 1
            else:
                word += i
                continue

        for i in range(l.count(" ")):
            l.remove(" ")

        print("NOTE :- Try to write the equal words in corresponds to the Paragraph", end=",")
        print("The Accuracy may vary a lot")
        print("Enter your words:- ")
        start = time.time()
        your_st = input()
        end = time.time()

        m = []
        for i in your_st:
            if i == " " or i == ".":
                m.append(word)
                word = ""
                word_count += 1
            else:
                word += i
                continue

        for i in range(m.count(" ")):
            m.remove(" ")

        correct = 0

        if len(l) > len(m):
            for i in range(len(l) - len(m)):
                m.append(" ")

        if len(l) < len(m):
            for i in range(len(m) - len(l)):
                m.pop()

        for i in range(len(l)):
            if l[i] == m[i]:
                correct += 1

        accuracy = correct/len(m)
        print("Time :- " + str(round(end - start, 2)) + "s")
        print("Accuracy :- " + str(round(accuracy, 2) * 100 ) + "%")

        dec = input("[Want to try more :- Y/n ]")
        if dec == "Y":
            repeat()
        else:
            exit()


    if decision == "n":
        print("OK !")
        dec = input("[Want to try more :- Y/n ]")
        if dec == "Y":
            repeat()
        else:
            exit()

def typing_test():
    clear()
    decision = input("[Want to try :- 'Y/n' ] ")

    if decision == "Y":
        file = open('paragraph.txt', 'r')
        Lines = file.readlines()
        st = random.choice(Lines)
        if st[-1] !=".":
            st += "."

        print("\n")
        print("Your Paragraph is here :-")

        print(st)
        word_count = 0
        l = []
        word = ""
        for i in st:
            if i == " " or i == ".":
                l.append(word)
                word = ""
                word_count += 1
            else:
                word += i
                continue

        for i in range(l.count(" ")):
            l.remove(" ")

        print("NOTE :- Try to write the equal words in corresponds to the Paragraph", end=",")
        print("The Accuracy may vary a lot")
        print("Enter your words:- ")
        start = time.time()
        your_st = input()
        end = time.time()

        m = []
        for i in your_st:
            if i == " " or i == ".":
                m.append(word)
                word = ""
                word_count += 1
            else:
                word += i
                continue

        for i in range(m.count(" ")):
            m.remove(" ")

        correct = 0

        if len(l) > len(m):
            for i in range(len(l) - len(m)):
                m.append(" ")

        if len(l) < len(m):
            for i in range(len(m) - len(l)):
                m.pop()

        for i in range(len(l)):
            if l[i] == m[i]:
                correct += 1

        accuracy = correct/len(m)
        Time = end - start
        print("Time :- " + str(round(end - start, 2)) + "s")
        print("Accuracy :- " + str(round(accuracy, 2) * 100 ) + "%")
        print("Words per minute :- " + str(round((len(m)/Time) * 60, 2)))

        dec = input("[Want to try more :- Y/n ]")
        if dec == "Y":
            repeat()
        else:
            exit()


    if decision == "n":
        print("OK !")
        dec = input("[Want to try more :- Y/n ]")
        if dec == "Y":
            repeat()
        else:
            exit()



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
        clear()
        decision = input("[Really Want to exit :- 'Y/n']")
        if decision == "Y":
            exit() # Exit
        if decision == "n":
            repeat() # repeat

# End of the code of typing test.
