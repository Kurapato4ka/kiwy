from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

class Root:
    pass 

class MyApp(App, Root):
    sm = ScreenManager()
    def build(self):
        self.title = Root.resources.get('title')
        return MyApp.sm