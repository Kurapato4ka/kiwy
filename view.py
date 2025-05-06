from root import Root
from screens import Scr_00, Scr_01, Scr_02, Scr_03, Scr_04, Error

class View(Root):
    def __init__(self):
        self.scr_00 = Scr_00()
        self.scr_01 = Scr_01()
        self.scr_02 = Scr_02()
        self.scr_03 = Scr_03()
        self.scr_04 = Scr_04()

        self.app.sm.add_widget(self.scr_00)
        self.app.sm.add_widget(self.scr_01)
        self.app.sm.add_widget(self.scr_02)
        self.app.sm.add_widget(self.scr_03)
        self.app.sm.add_widget(self.scr_04)


    def stage_00(self):
        self.app.sm.current = self.scr_00.name
    
    def stage_01(self):
        self.app.sm.current = self.scr_01.name

    def stage_02(self):
        self.app.sm.current = self.scr_02.name

    def stage_03(self):
        self.app.sm.current = self.scr_03.name

    def stage_04(self):
        self.app.sm.current = self.scr_04.name

    def stage_error(self, arg):
        error = Error(arg)

        

if __name__ == '__main__':
    pass

