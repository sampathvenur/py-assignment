print("enter your name: " )
name=input('name ')
print(name,':')


import random

def generate_quiz():
    # create a dictionary function to store all the qsns and answers of quiz
    questions_dict = {
        'topic1': {'question1': 'answer1', 'question2': 'answer2', 'question3': 'answer3', 'question4': 'answer4', 'question5': 'answer5','question6': 'answer6', 'question7': 'answer7', 'question8': 'answer9', 'question10': 'answer10','question11': 'answer11', 'question12': 'answer12', 'question13': 'answer13', 'question14': 'answer14', 'question15': 'answer15'},
        'topic2': {'question1': 'answer1', 'question2': 'answer2', 'question3': 'answer3', 'question4': 'answer4', 'question5': 'answer5','question6': 'answer6', 'question7': 'answer7', 'question8': 'answer9', 'question10': 'answer10','question11': 'answer11', 'question12': 'answer12', 'question13': 'answer13', 'question14': 'answer14', 'question15': 'answer15'},
        'topic3': {'question1': 'answer1', 'question2': 'answer2', 'question3': 'answer3', 'question4': 'answer4', 'question5': 'answer5','question6': 'answer6', 'question7': 'answer7', 'question8': 'answer9', 'question10': 'answer10','question11': 'answer11', 'question12': 'answer12', 'question13': 'answer13', 'question14': 'answer14', 'question15': 'answer15'},
        'topic4': {'question1': 'answer1', 'question2': 'answer2', 'question3': 'answer3', 'question4': 'answer4', 'question5': 'answer5','question6': 'answer6', 'question7': 'answer7', 'question8': 'answer9', 'question10': 'answer10','question11': 'answer11', 'question12': 'answer12', 'question13': 'answer13', 'question14': 'answer14', 'question15': 'answer15'}
    }

    # ask the user to choose a topic
    print("Choose a topic:")
    for i, topic in enumerate(questions_dict.keys(), 1):
        print(f"{i}. {topic}")
    topic_choice = int(input("Enter the number of your choice: "))
    topic = list(questions_dict.keys())[topic_choice - 1]

    # ask questions from the chosen topic
    questions = random.sample(list(questions_dict[topic].items()), 10)
    score = 0
    for i, (question, answer) in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct Answer!")
            score += 1
        else:
            print(f"Wrong! The  answer is {answer}.")

    print(f"Your final score is {score} out of {len(questions)}.")
    if (score>=5):
        print("CONGRATULATIONS "+name+" !...you won the game!!")
    else:
        print("better luck next time "+name+"...")    

generate_quiz()

