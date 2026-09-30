from questions.question import Question

# =====================================================
# TODO: Implement this class
# =====================================================

class MultipleSelectQuestion(Question):
    def __init__(self, title, prompt, points, choices, correct_choices):
        """
        correct_choices is a list of correct answer numbers.

        Example:
            correct_choices = [1, 2, 4]
        """
        # TODO 1:
        # Call the parent constructor using super().
        # Store choices and correct_choices as instance attributes.
        pass

    def display(self):
        # TODO 2:
        # Print the question title and prompt.
        # Print all choices with numbers.
        # Print a message saying: "Select all correct answers."
        pass

    def check_answer(self, user_answer):
        """
        Example input:
            "1, 2, 4"

        This should be converted into:
            [1, 2, 4]
        """

        # TODO 3:
        # Split the user_answer by commas.
        # Convert each part into an integer.
        # Be careful: the user may type spaces.
        #
        # Example:
        #   "1, 2, 4"
        # becomes:
        #   [1, 2, 4]

        # TODO 4:
        # Compare the user's selected choices with correct_choices.
        # Order does not matter, so compare them as sets:
        #   set(selected) == set(self.correct_choices)
        #
        # If the answer is exactly correct, return full points.
        # Otherwise, return 0 points.
        pass