###         Name:                 ###
###         Date:                 ###
###         Te Reo Quiz           ###

#This is the first function in this code. Where is chse the the variable related to the taks. Ask user 'Do you want to try again (Y/N)'
#I used if or else. If Y then the game loops again if N then the print message displays.

import random

def main():
    repeat = True
    print_welcome()
    while repeat == True:
        score = run_quiz()
        print_end(score)
        do_repeat = input("Do you want to try again? (Y/N) ")
        if do_repeat == "Y":
            repeat = True
        else:
            repeat = False
    print("Thanks for playing!")
    
#This is the second function - def print_welcome():
    border = "*" * 58
    print(border)
    print("* Kia ora and welcome to the Te Reo Maori Quiz!                      *")
    print("* Developed by [user]                                  *")
    print("*", "=" * 56, "*", sep="")
    print("* Guess the correct answers !              *")
    print("* Case sensitive*")
    print(border)
    
#def question and answers and using a while

def run_quiz():
    score = 0
    count = 0
    question = "What is the Maori word for "
    questions = ["one ? ", "two? ", "three? ", "four? ", "five? ", "six? ", "seven? ", "eight? ", "nine? ", "ten? ", "white? " , "red? ", "orange? ", "yellow? ", "green? ", "black? ", "blue? ", "purple? ", "brown? ", "grey? "]
    answers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau", "Ma", "Whero", "Karaka", "Kowhai", "Kakariki", "Mangu", "Kikorangi", "Waiporoporo", "Parauri", "Kiwikiwi"] 
    print()
    while count < 5:
        q_num = random.randint(0, len(questions) - 1)
        q_string = question + questions[q_num]
        user_answer = input(q_string)
        user_answer = user_answer.upper()
        if user_answer == answers[q_num]:
            score += 1
            print("Correct answer! Excellent!")
        else:
            print("Incorrect. The answer was: ", answers[q_num])
        print()
        count += 1
        questions.pop(q_num)
        answers.pop(q_num)
    return(score)

#This is the 4th function - show the score. Also finished off with the border *58 for * border. 5
def print_end(score):
    border = "*" * 58
    print(border)
    print("* You scored: ", score, "out of 5                                *")
    if score == 5:
        print("* Kia ora, Congratulations! You are aweseome!                        *")
    print(border)


main()

