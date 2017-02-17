
import json
import requests
from menu import menu
from util import utils

class tool:
    def __init__(self):
        self.api_path = 'http://www3.septa.org/hackathon/Arrivals/Suburban%20Station/{}/'
        self.num_trains = 5
        self.trains = []
        
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
        self.build_trains(req.json())
        for train in self.trains:
            print(train)
        
    def build_trains(self, json_data):
        self.trains = []
        key = list(json_data.keys())[0]
        train_directions = json_data[key]
        for direction in train_directions:
            for trains in direction:
                for train in direction[trains]:
                    self.trains.append(Train.from_dict(train))


class Train():
    def __init__(self, num, dest, track, track_change, pltfm, pltfm_change, expr, depart, late):
        self.num = num
        self.dest = dest
        self.track = track
        self.track_change = track_change
        self.pltfm = pltfm
        self.pltfm_change = pltfm_change
        self.expr = expr
        self.depart = depart
        self.late = late

    def __str__(self):
        string = "Train {} to {} at {}".format(self.num, self.dest, self.depart)
        return string if self.late == 'On Time' else utils.error_string(string)


    def from_dict(d):
        track_change = d['track_change']
        platform_change = d['platform_change']
        depart_time = d['depart_time']
        train = Train(d['train_id'], d['destination'], d['track'],
                track_change, d['platform'], platform_change, d['service_type'],
                depart_time, d['status'])
        return train
