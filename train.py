
from utils import text_util
from Datetime import Datetime

class Train():
    def __init__(self, num, dest, track, track_change, pltfm, pltfm_change, expr, depart, direction, late):
        self.num = num
        self.dest = dest
        self.track = track
        self.track_change = track_change
        self.pltfm = pltfm
        self.pltfm_change = pltfm_change
        self.expr = expr
        self.depart = depart
        self.direction = direction
        self.late = late

    def __str__(self):
        string = "Train {} to {} at {}".format(self.num, self.dest, self.depart)
        return string if self.on_time() else text_util.error_string(string)

    def get_display_strings(self):
        return  [self.num, self.dest, self.depart]

    def on_time(self):
        return self.late == 'On Time'

    def from_dict(d):
        track_change = d['track_change']
        platform_change = d['platform_change']
        depart_time = Datetime.from_api_string(d['depart_time'])
        
        train = Train(d['train_id'], d['destination'], d['track'],
                track_change, d['platform'], platform_change, d['service_type'],
                depart_time, d['direction'], d['status'])

        return train
