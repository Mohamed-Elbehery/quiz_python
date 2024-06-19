from quiz_brain import Quiz

username = input("\nEnter Your Name Please: ")

# * Initializing Object of the Quiz Class and giving it the username we got from the user"
quiz = Quiz(username)

# * Display each question and wait for the user to answer and check if the answer is "Correct" or "Wrong" and Evaluate the Score
for question in quiz.questions:
    isCorrect = quiz.ask_and_check_answer(quiz.question_number, question["text"])

    if bool(isCorrect):
        quiz.score += 1

    quiz.question_number += 1

# * Display the Grade of the Student
if quiz.score >= 6:
    print(f"\nCongratulations {quiz.username} Your Grade is : {quiz.score}/12")
else:
    print(f"\nHard Luck {quiz.username} Your Grade Unfortunatley is : {quiz.score}/12")
