import os
import random


def load_questions(filename="questions.txt"):
    questions = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                question_data = line.strip().split("|")
                questions.append(question_data)
    return questions


def save_questions(questions, filename="questions.txt"):
    with open(filename, 'w') as file:
        for question in questions:
            file.write("|".join(question) + "\n")


def play_quiz():
    questions = load_questions()
    if not questions:
        print("No questions available to play the quiz.")
        return

    score = 0
    random.shuffle(questions)  

    for question in questions:
        print("\nQuestion: " + question[0])
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = question[1].strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question[1]}")

    print(f"\nYour final score is {score}/{len(questions)}.")


def add_question():
    question_text = input("Enter the question: ")
    answer_text = input("Enter the answer: ")
    new_question = [question_text, answer_text]

    questions = load_questions()
    questions.append(new_question)
    save_questions(questions)

    print("Question added successfully.")

def view_questions():
    questions = load_questions()
    if questions:
        print("Quiz Questions List:")
        for index, question in enumerate(questions, 1):
            print(f"{index}. Question: {question[0]}")
            print(f"   Answer: {question[1]}")
    else:
        print("No questions available.")

def delete_question():
    questions = load_questions()
    if not questions:
        print("No questions available to delete.")
        return

    view_questions()
    try:
        question_index = int(input("Enter the question number to delete: ")) - 1
        if 0 <= question_index < len(questions):
            questions.pop(question_index)
            save_questions(questions)
            print("Question deleted successfully.")
        else:
            print("Invalid question number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def update_question():
    questions = load_questions()
    if not questions:
        print("No questions available to update.")
        return

    view_questions()
    try:
        question_index = int(input("Enter the question number to update: ")) - 1
        if 0 <= question_index < len(questions):
                new_question_text = input(f"Enter new question (Current: {questions[question_index][0]}): ")
                new_answer_text = input(f"Enter new answer (Current: {questions[question_index][1]}): ")
                questions[question_index] = [new_question_text, new_answer_text]
                save_questions(questions)
                print("Question updated successfully.")
        else:
            print("Invalid question number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_questions():
    questions = load_questions()
    if questions:
        print("Quiz Questions List:")
        for index, question in enumerate(questions, 1):
            print(f"{index}. Question: {question[0]}")
            print(f"   Answer: {question[1]}")
    else:
        print("No questions available.")

def main():
    while True:
        print("\nQuiz Game System Menu")
        print("1. Play Quiz Game")
        print("2. Add Question")
        print("3. View Questions")
        print("4. Delete Question")
        print("5. Update Question")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            view_questions()
        elif choice == '2':
            add_question()
        elif choice == '3':
            update_question()
        elif choice == '4':
            delete_question()
        elif choice == '5':
            play_quiz()
        elif choice == '6':
            print("Exiting the Quiz Game System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()