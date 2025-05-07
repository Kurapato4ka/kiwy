from root import Root
from kivy.clock import Clock


class Model(Root):
    def __init__(self):
        self.ruffier = self.Ruffier()
        self.timer_00 = self.Timer("timer_00",[(15, 1, -1, 0.25, 0)])

    
    class Ruffier:
        def __init__(self):
            self.data = dict()
            self.table = [[0, 0.5, 6, 11, 15, 100],
                     [0, 2, 7.5, 12.5, 16.5, 100],
                     [0, 3.5, 9, 14, 18, 100],
                     [0, 5, 10.5, 15.5, 19.5, 100],
                     [0, 6.5, 12, 17, 21, 100]
                    ]



                    

        def load_data(self, **arg):
            for key, value in arg.items():
                self.data[key] = value

        def result(self):
            if 7 <= self.data['age'] <= 8:
                age = 4
            elif 9 <= self.data['age'] <= 10:
                age = 3
            elif 11 <= self.data['age'] <= 12:
                age = 2
            elif 13 <= self.data['age'] <= 14:
                age = 1
            elif 15 <= self.data['age']:
                age = 0

            index = (4*(self.data['P1']+self.data['P2']+self.data['P3']) - 200)/10            
            for i in range(0, 4):
                if self.table[age][i] <= index <= self.table[age][i+1]:
                    break
            return (index, i)

        def check_pulse(self, arg):
            try:
                arg = int(arg)
            except:
                return (1,)
            if Model.resources.get('pulse_min') <= arg <= Model.resources.get('pulse_max'):
                return (0, arg)
            elif arg < Model.resources.get('pulse_min'):
                return (2,)
            elif Model.resources.get('pulse_max') < arg:
                return (3,)

        def check_age(self, arg):
            try:
                arg = int(arg)
            except:
                return (1,)
            if Model.resources.get('age_min') <= arg <= Model.resources.get('age_max'):
                return (0, arg)
            elif arg < Model.resources.get('age_min'):
                return (4,)
            elif Model.resources.get('age_max') < arg:
                return (5,)
            
    class Timer:
        def __init__(self, name, intervals):
            self.name = name
            self.intervals = intervals
            self.interval = 0
            
        def start(self):
            self.begin = self.intervals[self.interval][0]
            self.end = self.intervals[self.interval][1]
            self.step = self.intervals[self.interval][2]
            self.delay = self.intervals[self.interval][3]
            self.parameter = self.intervals[self.interval][4]
            self.tick()
            # Clock.schedule_once(self.tick, self.delay)
            
        def tick(self, *args):
            Model.controller.command((self.name, (self.begin, self.parameter)))
            self.begin += self.step
            if (self.step < 0 and self.begin < self.end) or (self.step > 0 and self.begin > self.end):
                if self.interval < len(self.intervals) -1:
                    self.interval += 1
                    self.start()
                else:
                    Model.controller.command((self.name, False))
            else:
                Clock.schedule_once(self.tick, self.delay)
    
            


if __name__ == '__main__':
    model = Model()
    model.ruffier.load_data(age = 9, P1= 26, P2 = 26, P3 = 26)
    print(model.ruffier.result())
    