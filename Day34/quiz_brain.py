class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.output = None

    def still_has_questions(self):
        """Check if there are questions remaining"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Move on to the next question and return a complete text for printing on canvas"""
        self.current_question = self.question_list[self.question_number]
        output = f"Q.{self.question_number + 1}: {self.current_question.text}"
        self.question_number += 1
        return output

    def check_answer(self, user_answer):
        """Check answer and return a complete text for printing scores"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        return f"{self.score}/{self.question_number}"
