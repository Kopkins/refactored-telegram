from utils import text_util
from abc import ABCMeta
from abc import abstractmethod

class Menu(metaclass=ABCMeta):
    def __init__(self, option_action_pairs):
        self.options = self.create_menu_options(option_action_pairs)

    def select_execute(self):
        op_nums = list(range(1, len(self.options) + 1))
        for i in op_nums:
            print(i, ")", self.options[i - 1].string)

        try:
            entry = int(input('==> '))
        except ValueError:
            text_util.clear_console()
            text_util.print_error('Input not a number')
            return
        try:
            text_util.clear_console()
            self.options[entry - 1].execute()
        except IndexError:
            text_util.print_error('Input is not in menu')

    @staticmethod
    @abstractmethod
    def create_menu_options(pairs):
        return

    class MenuItem():
        def __init__(self, string, func):
            self.string = string
            self.func = func

        def execute(self):
            self.func()
