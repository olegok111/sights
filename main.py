# -*- coding: utf-8 -*-
import dbwrite
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import NoTransition
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')


one_img_question = 0
four_img_question = 0
score = 0
lives = 3
current_player = 'nond'

sm = ScreenManager()


def console_debug_output(instance):
    print('Element', instance.text, 'built succesfully.')


def exit_action():
    exit(0)


def add_points(player, amount):
    prev_points = dbwrite.pget(player)['points']
    dbwrite.pwrite(player, prev_points+amount)


def life_count():
    global lives, sm
    lives -= 1
    if lives == 0:
        sm.transition = NoTransition()
        sm.current = 'main'
    print(lives)
    return lives


with open('structure.kv', encoding='utf8') as f:
    Builder.load_string(f.read())


class ImageButton(ButtonBehavior, Image): pass

class MainScreen(Screen): pass
class SettingsScreen(Screen): pass
class QuestChooseScreen(Screen): pass
class ZAO1(Screen): pass
class ZAO2(Screen): pass
class ZAO3(Screen): pass
class ZAO4(Screen): pass
class ZAO5(Screen): pass
class ZAO6(Screen): pass
class ZAO7(Screen): pass
class ZAO8(Screen): pass
class ZAO9(Screen): pass
class ZAO10(Screen): pass
class ZAO11(Screen): pass
class EndingScreen(Screen): pass


sm.add_widget(MainScreen(name='main'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(QuestChooseScreen(name='quests'))
sm.add_widget(ZAO1(name='qzao1'))
sm.add_widget(ZAO2(name='qzao2'))
sm.add_widget(ZAO3(name='qzao3'))
sm.add_widget(ZAO4(name='qzao4'))
sm.add_widget(ZAO5(name='qzao5'))
sm.add_widget(ZAO6(name='qzao6'))
sm.add_widget(ZAO8(name='qzao8'))
sm.add_widget(ZAO7(name='qzao7'))
sm.add_widget(ZAO9(name='qzao9'))
sm.add_widget(ZAO10(name='qzao10'))
sm.add_widget(ZAO11(name='qzao11'))
sm.add_widget(EndingScreen(name='ending_screen'))


class SightsApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    SightsApp().run()
