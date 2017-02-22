
import json
import requests
from ListMenu import ListMenu
from utils import text_util
from Train import Train
from Table import Table

class tool:
    def __init__(self):
        self.api_path = 'http://www3.septa.org/hackathon/Arrivals/{}/{}/'
        self.station_id = 90005
        self.num_trains = 5
        self.trains = []
        self.stations = []
        self.stations_file = 'groomed_stations.csv'
        
        menu_options = []
        menu_options.append(('List Trains', lambda : self.fetch_trains()))
        menu_options.append(('Select Station', lambda : self.select_station()))
        menu_options.append(('Set Number of Trains to Show',
                             lambda : self.count_limit()))
        menu_options.append(("Quit", lambda : exit()))
        self.main_menu = ListMenu(menu_options)


    def run_main_menu(self):
        text_util.clear_console()
        while True:
            self.main_menu.select_execute()

    def select_station(self):
        if len(self.stations) == 0:
            self.load_stations()
        station_opts = []
        for station in self.stations:
            station_opts.append((station[1], lambda : self.set_station(station[0])))
        station_menu = ListMenu(station_opts)
        station_menu.select_execute()


    def load_stations(self):
        with open(self.stations_file) as in_file:
            for line in in_file:
                id, name = line.strip().split(',')
                self.stations.append((id, name))
                

    def set_station(self, station_id):
        self.station_id = station_id

    def count_limit(self):
        self.num_trains = input('Trains to Display => ')

    def fetch_trains(self):
        req = requests.get(self.api_path.format(self.station_id, self.num_trains))
        self.build_trains(req.json())
        rows = [[train.num, train.dest, train.depart] for train in self.trains]
        table = Table(rows)
        print(table)
        
    def build_trains(self, json_data):
        self.trains = []
        key = list(json_data.keys())[0]
        train_directions = json_data[key]
        for direction in train_directions:
            for trains in direction:
                for train in direction[trains]:
                    self.trains.append(Train.from_dict(train))

