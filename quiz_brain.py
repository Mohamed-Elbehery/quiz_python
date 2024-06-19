from data import question_data

questions_bank = []

# * Initializing Objects of the Question Class using the "question_data" from "data" module
for question in question_data:
    questions_bank.append(question)


class Quiz:
    def __init__(self, username):
        self.questions = questions_bank
        self.score = 0
        self.question_number = 1
        self.question = self.questions[self.question_number - 1]
        self.username = username

    def ask_and_check_answer(self, question_number, text):
        answer = input(f"\n{question_number} - {text} (True/False)?: ")
        return self.question["answer"] == answer
