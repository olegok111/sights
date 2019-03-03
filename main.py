# -*- coding: utf-8 -*-
from kivy.app import App
import dbwrite
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
'''
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '1920')
'''


def console_debug_output(instance):
    print('Element', instance.text, 'built succesfully.')


def exit_action(instance):
    exit(0)


def add_10(instance):
    prev_points = dbwrite.pget(instance.text)['points']
    dbwrite.pwrite(instance.text, prev_points+10)


class ImageButton(ButtonBehavior, Image):
    pass


with open('structure.kv', encoding='utf8') as f:
    Builder.load_string(f.read())


class MainScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class QuestChooseScreen(Screen):
    pass


class QZAOBeginScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(QuestChooseScreen(name='quests'))
sm.add_widget(QZAOBeginScreen(name='qzaobegin'))


class SightsApp(App):
    question = NumericProperty(0)

    def build(self):
        return sm


if __name__ == '__main__':
    SightsApp().run()
