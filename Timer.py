import time
class TimerObject:
    def __init__(self, name, accum=0, interval=5):
        self._name = name
        self._accum = accum
        self._interval = interval
    
    @property
    def name(self):
        return self._name
    @property
    def accum(self):
        return self._accum
    @property
    def interval(self):
        return self._interval

    @name.setter
    def name(self, name):
        self._name = name
    
    @accum.setter
    def accum(self, accum):
        self._accum = accum
    
    @interval.setter
    def interval(self, interval):
        self._interval = interval
    
    def print_time(self, name, accum):
        msg = name + ': {accum}'.format(accum = accum)
        print(msg)
    
    def print_data(self):
        msg = 'name: {x}'.format(x=self.name)
        print(msg)
        msg = 'accum: {x}'.format(x=self.accum)
        print(msg)
        msg = 'interval: {x}'.format(x=self.interval)
        print(msg)
    
    def upCount(self, limit):
        spam = limit + 1
        name = self.name
        accum = self.accum
        interval = self.interval
        if limit % interval == 0:
            spam = limit + 1
            eggs = 0
            print('counting up on: ' + name)
            for interval in range(spam):
                while eggs < interval:
                    self.print_time(name, accum)
                    eggs += 1
                    accum += 1
                    time.sleep(1)
                self.accum = accum
            self.print_time(name, accum)
        elif limit % interval != 0:
            spam = int(limit / interval)
            eggs = 0
            print('counting up on: ' + name)
            for interval in range(spam):
                while eggs < interval:
                    self.print_time(name, accum)
                    eggs += 1
                    accum += 1
                    time.sleep(1)
                self.accum = accum
            self.print_time(name, accum)
    
    def downCount(self, limit):
        name = self.name
        accum = self.accum
        interval = self.interval
        if limit % interval == 0:
            spam = limit + 1
            eggs = 0
            duck = limit
            print('counting down on: ' + name)
            for interval in range(spam):
                while eggs < interval:
                    self.print_time(name, duck)
                    eggs += 1
                    accum -= 1
                    duck -= 1
                    time.sleep(1)
                self.accum = accum
            self.print_time(name, duck)
        elif limit % interval != 0:
            spam = int(limit / interval)
            eggs = 0
            duck = limit
            print('counting down on: ' + name)
            for interval in range(spam):
                while eggs < interval:
                    self.print_time(name, duck)
                    eggs += 1
                    accum -= 1
                    duck -= 1
                    time.sleep(1)
                self.accum = accum
            self.print_time(name, duck)

timer = TimerObject('test')
timer.upCount(6)
timer.downCount(6)
timer.print_data()