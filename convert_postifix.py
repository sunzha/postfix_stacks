# add documentation here
from data_structures.stack_adt import ArrayStack

operators = {"+": 1, "-": 1, "*": 2, "/": 2} # dictionary containing the operators and their ordering

def convert_to_postifx(infix_expression: str) -> str:
    """ Converts an infix expression to postifix expression
    
    :Input:
        infix_expression (str): The expression in infix notation
                        i.e. "a + b + c * d"
    
    :Returns:
        str: The expression in postfix notation
                        i.e. "a b + c d * +"
    
    :Complexity: O(n) where n is the length of the infix expression
    """
    raise NotImplementedError