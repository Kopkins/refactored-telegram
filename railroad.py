
import json
import requests
from menu import menu
from util import utils

class tool:
    def __init__(self):
        self.api_path = 'http://www3.septa.org/hackathon/Arrivals/Suburban%20Station/{}/'
        self.num_trains = 5
        self.filters = {}
        
        menu_options = []
        menu_options.append(('List Trains', lambda : self.fetch_trains()))
        menu_options.append(('Set Number of Trains to Show',
                            lambda : self.count_limit()))
        menu_options.append(("Quit", lambda : exit()))
        self.main_menu = menu(menu_options)


    def run_main_menu(self):
        utils.clear_console()
        while True:
            self.main_menu.select_execute()

    def pick_rail_line(self):
        pass

    def apply_filter(self, f, l):
        pass

    def count_limit(self):
        self.num_trains = input('Trains to Display => ')

    def fetch_trains(self):
        req = requests.get(self.api_path.format(self.num_trains))
        print(req.json())


class Train():
    def __init__(self):
        self.next_stop = None
        self.express = False
        self.destination = None
        self.late = None
