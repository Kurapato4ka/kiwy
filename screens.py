from root import Root 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class Scr_00(Root, Screen):
    def __init__(self):
        Screen.__init__(self, name = '00')
        self.setUI()
        self.setCMD()

    def setUI(self):
        get = self.resources.get
        self.layout = BoxLayout(orientation = 'vertical', spacing = 10)
        self.add_widget(self.layout)
        self.layoutH1 = BoxLayout(orientation = 'horizontal', size_hint =(1 , .75))
        self.layoutH2 = BoxLayout(orientation = 'horizontal', size_hint = (.5 , .05), pos_hint ={'right': .75})
        self.layoutH3 = BoxLayout(orientation = 'horizontal', size_hint = (.5 , .05), pos_hint ={'right': .75})
        self.layoutH4 = BoxLayout(orientation = 'horizontal', size_hint = (.3 , .15), pos_hint ={'right': .65})
        self.layout.add_widget(self.layoutH1)
        self.layout.add_widget(self.layoutH2)
        self.layout.add_widget(self.layoutH3)
        self.layout.add_widget(self.layoutH4)
        self.txt = Label(text = get('txt_instruction'))
        self.txt1 = Label(text = get('txt_name'))
        self.write = TextInput()
        self.txt2 = Label(text = get('txt_age'))
        self.write1 = TextInput()
        self.btn = Button(text = get('txt_begin'))
        self.layoutH1.add_widget(self.txt)
        self.layoutH2.add_widget(self.txt1)
        self.layoutH2.add_widget(self.write)
        self.layoutH3.add_widget(self.txt2)
        self.layoutH3.add_widget(self.write1)
        self.layoutH4.add_widget(self.btn)


    def setCMD(self):
        self.btn.on_press = lambda: self.controller.command(('next_01', (self.write.text, self.write1.text)))




class Scr_01(Root, Screen):
    def __init__(self):
        Screen.__init__(self, name = '01')
        self.setUI()
        self.setCMD()

    def setUI(self):
        get = self.resources.get
        self.layout = BoxLayout(orientation = 'vertical', spacing = 10)
        self.add_widget(self.layout)
        self.layoutH1 = BoxLayout(orientation = 'horizontal', size_hint =(1 , .55))
        self.layoutH2 = BoxLayout(orientation = 'horizontal', size_hint = (.5 , .15), pos_hint ={'right': .75})
        self.layoutH3 = BoxLayout(orientation = 'horizontal', size_hint = (.5 , .10), pos_hint ={'right': .75})
        self.layoutH4 = BoxLayout(orientation = 'horizontal', size_hint = (.5 , .05), pos_hint ={'right': .75})
        self.layoutH5 = BoxLayout(orientation = 'horizontal', size_hint = (.3 , .15), pos_hint ={'right': .65})
        self.layout.add_widget(self.layoutH1)
        self.layout.add_widget(self.layoutH2)
        self.layout.add_widget(self.layoutH3)
        self.layout.add_widget(self.layoutH4)
        self.layout.add_widget(self.layoutH5)
        self.txt = Label(text = get('txt_test1'))
        self.txt1 = Label(text = get('txt_result'))
        self.txt2 = Label(text = '0')
        self.write = TextInput()
        self.btn = Button(text = get('txt_continiu'))
        self.btn1 = Button(text = get('txt_starttest1'))
        self.layoutH1.add_widget(self.txt)
        self.layoutH2.add_widget(self.txt2)
        self.layoutH3.add_widget(self.btn1)
        self.layoutH4.add_widget(self.txt1)
        self.layoutH4.add_widget(self.write)
        self.layoutH5.add_widget(self.btn)

    def setCMD(self):
        self.btn.on_press = lambda: self.controller.command(('next_02', (self.write.text)))



class Scr_02(Root, Screen):
    def __init__(self):
        Screen.__init__(self, name = '02')
        self.setUI()
        self.setCMD()

    def setUI(self):
        get = self.resources.get
        self.layout = BoxLayout(orientation = 'vertical', spacing = 10)
        self.add_widget(self.layout)
        self.layoutH1 = BoxLayout(orientation = 'horizontal', size_hint =(1 , .60))
        self.layoutH2 = BoxLayout(orientation = 'horizontal', size_hint = (.5 , .15), pos_hint ={'right': .75})
        self.layoutH3 = BoxLayout(orientation = 'horizontal', size_hint = (.5 , .10), pos_hint ={'right': .75})
        self.layoutH4 = BoxLayout(orientation = 'horizontal', size_hint = (.3 , .15), pos_hint ={'right': .65})
        self.layout.add_widget(self.layoutH1)
        self.layout.add_widget(self.layoutH2)
        self.layout.add_widget(self.layoutH3)
        self.layout.add_widget(self.layoutH4)
        self.txt = Label(text = get('txt_test2'))
        self.txt2 = Label(text = '0')
        self.btn = Button(text = get('txt_continiu'))
        self.btn1 = Button(text = get('txt_starttest2'))
        self.layoutH1.add_widget(self.txt)
        self.layoutH2.add_widget(self.txt2)
        self.layoutH3.add_widget(self.btn1)
        self.layoutH4.add_widget(self.btn)


    def setCMD(self):
        self.btn.on_press = lambda: self.controller.command(('next_03', ))



class Scr_03(Root, Screen):
    def __init__(self):
        Screen.__init__(self, name = '03')
        self.setUI()
        self.setCMD()

    def setUI(self):
        get = self.resources.get
        self.layout = BoxLayout(orientation = 'vertical', spacing = 10)
        self.add_widget(self.layout)
        self.layoutH1 = BoxLayout(orientation = 'horizontal', size_hint =(1 , .50))
        self.layoutH2 = BoxLayout(orientation = 'horizontal', size_hint = (.5 , .15), pos_hint ={'right': .75})
        self.layoutH3 = BoxLayout(orientation = 'horizontal', size_hint = (.5 , .10), pos_hint ={'right': .75})
        self.layoutH4 = BoxLayout(orientation = 'horizontal', size_hint = (.65 , .05), pos_hint ={'right': .75})
        self.layoutH5 = BoxLayout(orientation = 'horizontal', size_hint = (.65 , .05), pos_hint ={'right': .75})
        self.layoutH6 = BoxLayout(orientation = 'horizontal', size_hint = (.3 , .15), pos_hint ={'right': .65})
        self.layout.add_widget(self.layoutH1)
        self.layout.add_widget(self.layoutH2)
        self.layout.add_widget(self.layoutH3)
        self.layout.add_widget(self.layoutH4)
        self.layout.add_widget(self.layoutH5)
        self.layout.add_widget(self.layoutH6)
        self.txt = Label(text = get('txt_test3'))
        self.txt1 = Label(text = get('txt_result'))
        self.txt2 = Label(text = get('txt_result1'))
        self.txt3 = Label(text = '0')
        self.write = TextInput()
        self.write1 = TextInput()
        self.btn = Button(text = get('txt_stop'))
        self.btn1 = Button(text = get('txt_starttest3'))
        self.layoutH1.add_widget(self.txt)
        self.layoutH2.add_widget(self.txt3)
        self.layoutH3.add_widget(self.btn1)
        self.layoutH4.add_widget(self.txt1)
        self.layoutH4.add_widget(self.write)
        self.layoutH5.add_widget(self.txt2)
        self.layoutH5.add_widget(self.write1)
        self.layoutH6.add_widget(self.btn)


    def setCMD(self):
        self.btn.on_press = lambda: self.controller.command(('next_04', (self.write.text, self.write1.text)))



class Scr_04(Root, Screen):
    def __init__(self):
        Screen.__init__(self, name = '04')
        self.setUI()
        self.setCMD()

    def setUI(self):
        get = self.resources.get
        self.layout = BoxLayout(orientation = 'vertical', spacing = 10)
        self.layoutH2 = BoxLayout(orientation = 'horizontal')
        self.layoutH3 = BoxLayout(orientation = 'horizontal')
        self.add_widget(self.layout)
        self.layout.add_widget(self.layoutH2)
        self.layout.add_widget(self.layoutH3)
        self.txt = Label(text = get('txt_index'))
        self.txt1 = Label(text = get('txt_workheart'))
        self.layoutH2.add_widget(self.txt)
        self.layoutH3.add_widget(self.txt1)


    def setCMD(self):
        pass

    def stage_00(self, arg):
        get = self.resources.get
        index, line = arg
        self.txt.text = get('txt_index') + str(index)
        self.txt1.text = get('txt_workheart') + get('txt_res')[line]

class Error(Root, Popup):
    def __init__(self, error_number):
        Popup.__init__(self,title = self.resources.get('txt_error_title'), size_hint = (None, None), size =(500, 500))
        self.error_number = error_number
        self.setUI()
        self.setCMD()


    def setUI(self):
        get = self.resources.get
        self.layout = BoxLayout(orientation = 'vertical', spacing = 10)
        self.add_widget(self.layout)
        self.txt = Label(text = get('errors')[self.error_number])
        self.btn = Button(text = get('txt_cancel'))
        self.layout.add_widget(self.txt)
        self.layout.add_widget(self.btn)
        self.open()
     

    def setCMD(self):
        def close():
            self.dismiss()

        self.btn.on_release = close

