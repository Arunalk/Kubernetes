from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"] 
    question_answer = question["answer"]  
    q1 = Questions(question_text, question_answer)  
    question_bank.append(q1)

question_list = QuizBrain(question_bank)
while question_list.still_has_questions():
    question_list.next_question()

print(f"You've completed the quiz\nYour Final Score was: {question_list.score}/{question_list.question_number}")
