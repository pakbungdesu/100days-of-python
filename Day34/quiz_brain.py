class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.output = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        output = f"Q.{self.question_number + 1}: {self.current_question.text}"
        self.question_number += 1
        return output

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        result = 0
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            result = 1

        return [result, f"{self.score}/{self.question_number}"]
