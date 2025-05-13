class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.questions} (True/False)\n")
        self.check_answers(user_answer, current_question.answers)

    def check_answers(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score +=1
            print("You got it right")
        else:
            print(f"That's worng (:")
        print(f"The correct answer is: {answer}\nYour Current Score: {self.score}/{self.question_number}\n")
            



