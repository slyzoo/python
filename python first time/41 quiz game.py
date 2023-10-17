#---------------------------------------------------------------------------------------------------

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






#---------------------------------------------------------------------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print("#---------------------------------------------------------------------------------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        guess = input("enter A, B, C, D: ")
        guess = guess.upper()
        guesses.append(guess)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        correct_guesses += check_answer(questions.get(key),guess)
        question_number += 1

    display_score(correct_guesses, guesses)

#---------------------------------------------------------------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("INCORRECT")
        return 0
#---------------------------------------------------------------------------------------------------
def display_score(correct_guesses, guesses):
    print("#---------------------------------------------------------------------------------------------------")
    print("RESULTS")
    print("#---------------------------------------------------------------------------------------------------")

    print("answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end=" ")
    for i in guesses:
            print(i, end=" ")
    print()


    score = int((correct_guesses/len(questions))*100)
    print("your score is " + str(score) + "%")

#---------------------------------------------------------------------------------------------------

def play_again():
    
    response = input("do you wanna play again?: (yes / no)")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
    "who is the creator of fnaf?": "A",                 
    "who is the robot chicken in fnaf?": "B",           
    "who is gold in fnaf?": "D",                        
    "how did william afton die? (the first time)": "D", 
    "how many godzilla forms are there?": "C",           
    "how many godzilla movies are there as of 2023": "D"
    }

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

options = [["A. scott cawthon" , "B. mark zuckerburg" , "C. elon musk", "D. mr.beast"] , #1
           ["A. foxy" , "B. chica" , "C. freddy" , "D. bonnie"] , #2
           ["A. freddy / bonnie" , "B. bonnie / foxy" , "C. foxy / freddy" , "D. golden freddy / golden bonnie" ] , #3
           ["A. heart attack" , "B. spikes" , "C. fire" , "D. springlock suit"  ] , #4
           ["A. 8" , "B. 100" , "C. 5" , "D. 27" ] , #5
           ["A. 24" , "B. 96" , "C. 27" , "D. 37"  ]   #6

]


new_game()

while play_again():
    new_game()


print("byeeeeee")