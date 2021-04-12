from operators import operator


@operator.Operator.register_operator
class Multiplication(operator.Operator):
    """
        The multiplication operator, this operator allows us to multiply two numbers together
    """
    def __init__(self):
        super().__init__('*')

    def act(self, x: int, y: int) -> int:
        return x * y