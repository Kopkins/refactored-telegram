
from Menu import Menu

class TableMenu(Menu):

    @staticmethod
    def create_menu_options(pairs):
        column_widths = TableMenu.get_formatting([pair[0] for pair in pairs])
        menu_items = []
        for pair in pairs:
            values = pair[0]
            strings = [('{:{}}  '.format(values[i], column_widths[i])) for i in range(0, len(values))]
            menu_items.append(Menu.MenuItem(''.join(strings), pair[1]))
        return menu_items
                

    @staticmethod
    def get_formatting(rows):
        columns = [[row[i] for row in rows] for i in range(0, len(rows[0]))]
        widths = [(max(len(value) for value in column)) for column in columns]

        return widths

