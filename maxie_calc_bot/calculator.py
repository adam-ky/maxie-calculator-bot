import logging
from typing import Type

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


class Calculator:
    SYNTAX_ERR_MSG = "Oops, looks like your expression is invalid!"
    ZERO_DIV_ERR_MSG = "You can't divide by zero, dummy!"
    NAME_ERR_MSG = "Please only include values provided by the keyboard!"
    input = ""

    def get_input(self):
        return self.input

    def add_input(self, val):
        self.input += val

    def clear_input(self):
        self.input = ""

    def backspace_input(self):
        self.input = self.input[:-1]

    def evaluate(self):
        try:
            result = eval(self.input)
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.input = str(result)

            logger.info("Expression evaluated to: %f", result)

            return self.input

        except SyntaxError as e:
            logger.info(e)
            return Calculator.SYNTAX_ERR_MSG

        except ZeroDivisionError as e:
            logger.info(e)
            return Calculator.ZERO_DIV_ERR_MSG

        except NameError as e:
            logger.info(e)
            return Calculator.NAME_ERR_MSG

        except TypeError as e:
            logger.info(e)
            return Calculator.SYNTAX_ERR_MSG
