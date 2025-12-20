class Question:
    """
    Models a single quiz question.

    Attributes:
        text (str): The actual question/statement to be displayed.
        answer (str): The correct answer to the question (e.g., "True" or "False").
    """

    def __init__(self, q_text, q_answer):
        """
        Initializes the question object with a statement and its corresponding answer.

        Args:
            q_text (str): The string of text for the question.
            q_answer (str): The expected answer for the question.
        """
        self.text = q_text
        self.answer = q_answer
