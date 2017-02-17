
class menu():
    def __init__(self, option_action_pairs):
        self.options = [menu_item(string, func) for string, func in option_action_pairs]

    def select_execute(self):
        op_nums = list(range(1, len(self.options) + 1))
        for i in op_nums:
            print(i, ")", self.options[i - 1].string)

        entry = int(input())
        if entry not in op_nums:
            print('Invalid input')
            return None
        else: 
            self.options[entry - 1].execute()


class menu_item():
    def __init__(self, string, executor):
        self.string = string
        self.executor = executor

    def execute(self):
        self.executor()
