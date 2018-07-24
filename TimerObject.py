import time
class TimerObject:
    class_name = ""
    accum = 0
    interval = 0
    balance = 0
    
    def __init__(self, name, accum=0, interval=5, balance=0):
        self._name = name
        self._accum = accum
        self._interval = interval
        self._balance = balance
    
    @property
    def name(self):
        return self._name
    
    @property
    def accum(self):
        return self._accum
    
    @property
    def interval(self):
        return self._interval
    
    @property
    def balance(self, balance):
        return self._balance
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @accum.setter
    def accum(self, accum):
        self._accum = accum
    
    @interval.setter
    def interval(self, interval):
        self._interval = interval
    
    def print_data(self, name, accum):
        msg = name + ': {accum}'.format(accum = accum)
        print(msg)

    def upCount(self):
        name = self.name
        accum = self.accum
        interval = self.interval
        temp = 0
        print('counting up on: ' + name)
        self.print_data(name, accum)
        stop = false
        while stop == false:
            if accum >= limit:
                stop = true
            elif temp < interval:
                time.sleep(1)
                temp += 1
                accum += 1
                self.print_data(name, accum)
            self.accum = accum
    
    def downCount(self):
        name = self.name
        accum = self.accum
        interval = self.interval
        print('counting down on: ' + name)
        self.print_data(name, accum)
        while accum > 0:
            time.sleep(1)
            accum -= 1
            self.print_data(name, accum)
        self.accum = accum

timer = TimerObject('test')
str = 'name: {x}'.format(x=timer.name)
str = 'accum: {x}'.format(x=timer.accum)
str = 'interval: {x}'.format(x=timer.interval)
timer.upCount()
timer.downCount()
timer.upCount()
timer.upCount()
timer.downCount()