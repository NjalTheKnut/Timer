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
    
    def print_accum(self, name, accum):
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
        eggs = 0
        print('counting up on: ' + name)
        for interval in range(spam):
            while eggs < interval:
                self.print_accum(name, accum)
                time.sleep(1)
                eggs += 1
                accum += 1
                self.accum = accum
        self.print_accum(name, accum)
    
    def downCount(self, limit):
        spam = limit + 1
        name = self.name
        accum = self.accum
        interval = self.interval
        eggs = 0
        print('counting down on: ' + name)
        for interval in range(spam):
            while eggs < interval:
                self.print_accum(name, accum)
                time.sleep(1)
                eggs += 1
                accum -= 1
            self.accum = accum
        self.print_accum(name, accum)

timer = TimerObject('test')
timer.upCount(10)
timer.downCount(5)
timer.print_data()