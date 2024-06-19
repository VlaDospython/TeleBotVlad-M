class Question:
    def __init__(self, question: str, options: list[str], correct: int):
        """

        :param question: Текстове формулювання запитання
        :param options: Варіанти відповідей
        :param correct: Індекс правильної відповіді
        """
        self.question = question
        self.options = options
        self.correct = correct