import time
class Time:
    def __init__(self):
        self.DeltaTime = 0
        self.time = time.time()
    def UpdateTimesStuff(self):
        #update deltatime
        time2 = time.time()
        self.DeltaTime = time2-self.time
        self.time = time2