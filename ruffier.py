from root import MyApp, Root
from resources import Resources
from model import Model
from view import View
from controller import Controller

Root.app = MyApp()
Root.resources = Resources()
Root.controller = Controller()
Root.view = View()
Root.model = Model()

Root.controller.start()
Root.app.run()
