class QuizBrain:
    """
    The engine of the quiz. Manages the question sequence,
    tracks the score, and validates answers.
    """

    def __init__(self, q_list):
        """
        Initializes the quiz brain with a list of Question objects.

        Args:
            q_list (list): A list containing Question objects from the question bank.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.output = None

    def still_has_questions(self):
        """
        Checks if there are still questions remaining in the list.

        Returns:
            bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next question from the list and formats it for display.

        Returns:
            str: The formatted question string (e.g., 'Q.1: Is the earth flat?').
        """
        self.current_question = self.question_list[self.question_number]
        output = f"Q.{self.question_number + 1}: {self.current_question.text}"
        self.question_number += 1
        return output

    def check_answer(self, user_answer):
        """
        Validates the user's answer against the correct answer.

        Args:
            user_answer (str): The answer provided by the user ('True' or 'False').

        Returns:
            list: A list containing:
                  - index 0 (int): 1 if correct, 0 if incorrect.
                  - index 1 (str): The current score status (e.g., '3/5').
        """
        correct_answer = self.current_question.answer
        result = 0
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            result = 1

        return [result, f"{self.score}/{self.question_number}"]
