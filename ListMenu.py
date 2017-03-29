
from menu import Menu
from utils import text_util

class ListMenu(Menu):


    @staticmethod
    def create_menu_options(pairs):
        return [Menu.MenuItem(string, func) for string, func in pairs]
