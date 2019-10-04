from math import pi, e
from simpleeval import simple_eval, NameNotDefined

constants = {'pi': str(pi),
             'e': str(e)}


def evaluate(expression):
    expression = expression.replace('pi', constants['pi'])
    expression = expression.replace('e', constants['e'])
    try:
        result = simple_eval(expression)
    except NameNotDefined:
        result = 'Evaluation error. Next time use numbers and math operators +, -, *, /'
    return result
