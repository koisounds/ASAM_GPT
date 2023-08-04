import datetime

class Time:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.cutoff = now - datetime.timedelta(minutes=15)



def check_last_modified(self):
    return self.now < self.cutoff
