from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from modules.persons import Persons


class BMIScreen(Screen):
    pass


class FormScreen(Screen):
    pass


class BMI(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        builder = Builder.load_file('bmi.kv')

        persons = Persons()
        builder.ids.navigation.ids.tab_manager.screens[1].add_widget(persons)

        return builder


BMI().run()