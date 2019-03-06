# -*- coding: utf-8 -*-
from kivy.app import App
import dbwrite
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
'''
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '1920')
'''

one_img_question = 0
four_img_question = 0
score = 0


def console_debug_output(instance):
    print('Element', instance.text, 'built succesfully.')


def exit_action(instance):
    print('{} caused exitus.'.format(str(instance.id)))
    print(instance)
    exit(0)


def add_points(instance, player, amount):
    prev_points = dbwrite.pget(player)['points']
    dbwrite.pwrite(player, prev_points+amount)


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


class ZAO1(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(QuestChooseScreen(name='quests'))


class SightsApp(App):

    def build(self):

        return sm


if __name__ == '__main__':
    SightsApp().run()