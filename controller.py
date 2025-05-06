from root import Root

class Controller(Root):
    def __init__(self):
        pass


    def start(self):
        self.command(('start', ))

    def command(self, reqeust):
        cmd = reqeust[0]
        if len(reqeust) == 2:
            arg = reqeust[1]
        else:
            arg = ''

        print(f'command: {cmd: <20}{arg}')
        if cmd == 'start':
            self.view.stage_00()

        elif cmd == 'next_01':
            check_age = self.model.ruffier.check_age(arg[1])
            if check_age[0] == 0:
                self.model.ruffier.load_data(age = check_age[1], name = arg[0])
                self.view.stage_01()
            else:
                self.view.stage_error(check_age[0])
                

        elif cmd == 'next_02':
            check_pulse = self.model.ruffier.check_pulse(arg[1])
            if check_pulse[0] == 0:
                    self.model.ruffier.load_data(P1 = check_pulse[1])
                    self.view.stage_02()
            else:
                self.view.stage_error(check_pulse[0])

        

        
            
