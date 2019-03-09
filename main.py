# -*- coding: utf-8 -*-
from kivy.app import App
import dbwrite
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import NoTransition
'''
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '1920')
'''

one_img_question = 0
four_img_question = 0
score = 0
lives = 3

sm = ScreenManager()

def console_debug_output(instance):
    print('Element', instance.text, 'built succesfully.')


def exit_action(instance):
    exit(0)


def add_points(instance, player, amount):
    prev_points = dbwrite.pget(player)['points']
    dbwrite.pwrite(player, prev_points+amount)


def life_count(instance):
    global lives, sm
    lives -= 1
    if lives == 0:
        sm.transition = NoTransition()
        sm.current = 'main'
    print(lives)
    return lives


class ImageButton(ButtonBehavior, Image):
    pass


with open('structure.kv', encoding='utf8') as f:
    Builder.load_string(f.read())


class MainScreen(Screen): pass
class SettingsScreen(Screen): pass
class QuestChooseScreen(Screen): pass
class ZAO1(Screen): pass
class ZAO2(Screen): pass
class ZAO3(Screen): pass
class ZAO4(Screen): pass
class ZAO4A(Screen): pass
class EndingScreen(Screen): pass


sm.add_widget(MainScreen(name='main'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(QuestChooseScreen(name='quests'))
sm.add_widget(ZAO1(name='qzao1'))
sm.add_widget(ZAO2(name='qzao2'))
sm.add_widget(ZAO3(name='qzao3'))
sm.add_widget(ZAO4(name='qzao4'))
sm.add_widget(ZAO4A(name='qzao4a'))
sm.add_widget(EndingScreen(name='ending_screen'))


class SightsApp(App):
    score = NumericProperty(0)

    def build(self):

        return sm


if __name__ == '__main__':
    SightsApp().run()