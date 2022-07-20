'''
Program gives user theory, revision work and a test.
After user completes the test, the program grades it.

Teacher has the option to add extra theory, revision work or tests.

Program made by: DP1-1 Mikus Bumburs
'''
# NEXT UPDATE ADD THEORY TOPIC SEPERATION
# ADD WORDED ANSWERS TO TEST

import os
import sys
import time


# Allows user to select which theory to learn.
def theory_selection():
    os.system('cls')
    with open(os.path.join(sys.path[0], "data/Theory.txt"), 'r') as full_list:
        theory_list = [line.split("'") for line in full_list]
    print('Avalible theory:\n')
    for i in range(len(theory_list)):
        print(i + 1, '. ', theory_list[i][0], sep="")
    print(len(theory_list) + 1, '. Return', sep='')
    theory_choice = int(input('\nChoose an option: '))
    if theory_choice == len(theory_list) + 1:
        start()
    os.system('cls')
    print(theory_list[theory_choice-1][2])
    input()
    theory_selection()


# Allows user to select which revision they'd like to do.
def revision_selection():
    os.system('cls')
    with open(os.path.join(sys.path[0], "data/Revision.txt"), 'r') as full_list:
        revision_list = [line.split("'") for line in full_list]
    print('Avalible revision:\n')
    for i in range(len(revision_list)):
        print(i + 1, '. ', revision_list[i][0], sep="")
    print(len(revision_list) + 1, '. Return', sep='')
    revision_choice = int(input('\nChoose an option: '))
    if revision_choice == len(revision_list) + 1:
        start()
    os.system('cls')
    print(revision_list[revision_choice-1][2])
    user_answer = int(input('Answer: '))
    if user_answer == int(revision_list[revision_choice-1][4]):
        print('Correct!')
    else:
        print('Incorrect. Right answer:', revision_list[revision_choice-1][4])
    input()
    revision_selection()


# Allows user to select which test to do.
def test_selection():
    os.system('cls')
    with open(os.path.join(sys.path[0], "data/Test.txt"), 'r') as full_list:
        test_list = [line.split("'") for line in full_list]
    print('Avalible tests:\n')
    for i in range(len(test_list)):
        print(i + 1, '. ', test_list[i][0], sep="")
    print(len(test_list) + 1, '. Return', sep='')
    test_choice = int(input('\nChoose an option: '))
    if test_choice == len(test_list) + 1:
        start()
    test_len = int(test_list[test_choice-1][2])
    os.system('cls')
    print('NOTE: Seperate fractions using a .')
    theory_name = test_list[test_choice-1][0]
    total_points = 0
    max_points = 0
    list_arg = 0
    for i in range(test_len):
        print(test_list[test_choice-1][4+list_arg])
        user_answer = str(input('Answer: '))
        if user_answer == test_list[test_choice-1][6+list_arg]:
            total_points = total_points + \
                int(test_list[test_choice-1][8+list_arg])
        max_points = max_points + int(test_list[test_choice-1][8+list_arg])
        list_arg = list_arg + 6
        os.system('cls')
    user_name = input('Name: ')
    add_results(user_name, theory_name, total_points, max_points)
    print('Total points:', total_points, 'out of', max_points)
    input()
    test_selection()


# Allows user with password to add theory, revision work or tests and review user results on tests.
def teacher_mode():
    os.system('cls')
    if int(input('Please enter the password: ')) == 420:
        os.system('cls')
        print('Teacher mode options:\n\n\
        1. Review test results \n\
        2. Add a theory \n\
        3. Add revision work \n\
        4. Add a test\n\
        5. Return')
        teacher_choice = int(input('Choose an option: '))
        if teacher_choice == 1:
            os.system('cls')
            with open(os.path.join(sys.path[0], "data/Results.txt"), 'r', encoding='utf-8') as full_list:
                user_list = [line.split("'") for line in full_list]
            for i in range(len(user_list)):
                print(i, '. ', user_list[i][0], sep="", end=': ')
                print(user_list[i][2], ' - ', user_list[i][4], sep="")
            input('Press ENTER to return')
            teacher_mode()
        elif teacher_choice == 2:
            theory_name = input('Theory topic: ')
            theory_text = input('Theory: \n')
            add_theory(theory_name, theory_text)
        elif teacher_choice == 3:
            revision_topic = input('Revision topic: ')
            revision_question = input('Revision question: ')
            revision_answer = input('Answer: ')
            add_revision(revision_topic, revision_question, revision_answer)
        elif teacher_choice == 4:
            test_topic = input('Test topic: ')
            test_question_count = int(input('Question count: '))
            add_test(test_topic, test_question_count)
        elif teacher_choice == 5:
            start()
        else:
            print('\n     Error\nPlease try again.')


# Add theory to system.
def add_theory(theory_name, theory_text):
    with open(os.path.join(sys.path[0], "data/Theory.txt"), 'a', encoding='utf-8') as full_list:
        full_list.write(
            "\n{}'],['{}".format(theory_name, theory_text))
    start()


# Add revision to system.
def add_revision(revision_topic, revision_question, revision_answer):
    with open(os.path.join(sys.path[0], "data/Revision.txt"), 'a', encoding='utf-8') as full_list:
        full_list.write(
            "\n{}'],['{}'],['{}".format(revision_topic, revision_question, revision_answer))
    start()


# Add test to system.
def add_test(test_topic, test_question_count):
    with open(os.path.join(sys.path[0], "data/Test.txt"), 'a', encoding='utf-8') as full_list:
        full_list.write(
            "\n{}'],['{}".format(test_topic, test_question_count))
        for i in range(test_question_count):
            question = input(f'Question {i+1}: ')
            answer = input(f'Answer {i+1}: ')
            points = input('Points: ')
            os.system('cls')
            full_list.write(
                "'],['{}'],['{}'],['{}".format(question, answer, points))
    start()


# Saves user results into a file.
def add_results(user_name, theory_name, total_points, max_points):
    with open(os.path.join(sys.path[0], "data/Results.txt"), 'a', encoding='utf-8') as full_list:
        full_list.write(
            "\n{}'],['{}'],['{}/{}".format(user_name, theory_name, total_points, max_points))


# Main choice for user, to select next function.
def start():
    os.system('cls')
    print('Welcome to MathTutor\n\nAvailable options:\n\
    1. Theory \n\
    2. Revision \n\
    3. Test \n\
    4. Teacher mode\n\
    5. Exit')
    choice = int(input('Please choose todays work: '))
    if choice == 1:
        theory_selection()
    elif choice == 2:
        revision_selection()
    elif choice == 3:
        test_selection()
    elif choice == 4:
        teacher_mode()
    elif choice == 5:
        exit()
    else:
        print('\n     Error\nPlease try again.')
        time.sleep(2)
        start()
        os.system('cls')


start()

# Currect program version
__version__ = 2
