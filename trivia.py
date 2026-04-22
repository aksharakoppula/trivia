from lists import questions, choices, answers
import random

# check index of user guess if it is contained in answers list

chosen = []
options = ['a', 'b', 'c', 'd']
correct = 0

def print_choices(my_choices):
    for i in range (len(my_choices)):
        letter = 'a'
        if i == 1:
            letter = 'b'
        elif i == 2:
            letter = 'c'
        elif i == 3:
            letter = 'd'
        print(f"{letter}: {my_choices[i]}")
        
def get_question():
    if len(chosen) == len(questions):
        return False
    question = random.choice(questions)
    while questions.index(question) in chosen:
        question = random.choice(questions)
    chosen.append(questions.index(question))
    return question

def get_answer(question,answer):
    global correct
    if answers[questions.index(question) ] == options.index(answer.lower()):
       print("That is correct!")
       correct += 1
    else:
       print("Sorry, wrong answer!")
       print(f"The answer was: {choices[questions.index(question)][answers[questions.index(question) ]]}")

running = True
while running:
    question = get_question()
    if not question:
        running = False
        continue
    print(question)
    my_choices = choices[questions.index(question)]
    print_choices(my_choices)
    answer = input("\nPlease enter your guess: ")
    while not answer.lower() in options:
        answer = input("\nPlease enter a valid guess: ")
    get_answer(question,answer)
    
        
print(f"This was your score:{correct}/20")
