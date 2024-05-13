import random

def generate_quiz():
    questions_dict = {
        'topic1': {'question1': 'answer1', 'question2': 'answer2', 'question3': 'answer3', 'question4': 'answer4', 'question5': 'answer5','question6': 'answer6', 'question7': 'answer7', 'question8': 'answer9', 'question9': 'answer9','question10': 'answer10','question11': 'answer11', 'question12': 'answer12', 'question13': 'answer13', 'question14': 'answer14', 'question15': 'answer15'},
        'topic2': {'question1': 'answer1', 'question2': 'answer2', 'question3': 'answer3', 'question4': 'answer4', 'question5': 'answer5','question6': 'answer6', 'question7': 'answer7', 'question8': 'answer9', 'question9': 'answer9','question10': 'answer10','question11': 'answer11', 'question12': 'answer12', 'question13': 'answer13', 'question14': 'answer14', 'question15': 'answer15'},
        'topic3': {'question1': 'answer1', 'question2': 'answer2', 'question3': 'answer3', 'question4': 'answer4', 'question5': 'answer5','question6': 'answer6', 'question7': 'answer7', 'question8': 'answer9', 'question9': 'answer9','question10': 'answer10','question11': 'answer11', 'question12': 'answer12', 'question13': 'answer13', 'question14': 'answer14', 'question15': 'answer15'},
        'topic4': {'question1': 'answer1', 'question2': 'answer2', 'question3': 'answer3', 'question4': 'answer4', 'question5': 'answer5','question6': 'answer6', 'question7': 'answer7', 'question8': 'answer9', 'question9': 'answer9','question10': 'answer10','question11': 'answer11', 'question12': 'answer12', 'question13': 'answer13', 'question14': 'answer14', 'question15': 'answer15'}
    }

    # Ask the user to choose a topic
    while True:
        print("Choose a topic:")
        for i, topic in enumerate(questions_dict.keys(), 1):
            print(f"{i}. {topic}")
        try:
            topic_choice = int(input("Enter the number of your choice: "))
            if topic_choice < 1 or topic_choice > len(questions_dict):
                raise ValueError("Invalid choice! Please enter a number within the given range.")
            break  # Break the loop if valid input is provided
        except ValueError as ve:
            print(ve)

    topic = list(questions_dict.keys())[topic_choice - 1]

    # Ask questions from the chosen topic
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
    if score >= 5:
        print("CONGRATULATIONS! You won the game!!")
    else:
        print("Better luck next time...")

generate_quiz()
