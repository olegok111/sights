# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import dbwrite
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
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

'''
class TestApp(App):

    def build(self):
        global sm
        all_scr_lyt = FloatLayout()
        button_exit = Button(text='X', font_size=72, background_color=[1, 0, 0, 1], background_normal='',
                             pos=(680, 510), size_hint=(.15, .15), on_press=exit_action)
        main_btn_lyt = BoxLayout(orientation='vertical', padding=[120], spacing=40,
                                 pos=(0, 0), size_hint=(1, .85))
        btn_1 = Button(text='Продолжить', on_press=console_debug_output)
        btn_2 = Button(text='Сменить игрока', on_press=self.trans)
        btn_3 = Button(text='nond', on_press=add_10)
        all_scr_lyt.add_widget(button_exit)
        main_btn_lyt.add_widget(btn_1)
        main_btn_lyt.add_widget(btn_2)
        main_btn_lyt.add_widget(btn_3)
        all_scr_lyt.add_widget(main_btn_lyt)

        self.sm = ScreenManager()
        menu_scr = Screen(name='menu')
        menu_scr.add_widget(all_scr_lyt)
        self.sm.add_widget(menu_scr)

        empty_scr = Screen(name='empty')
        self.sm.add_widget(empty_scr)
        empty_scr.add_widget(Button(text='test', on_press=self.trans))

        self.screens = [menu_scr, empty_scr]
        self.screen_number = 0
        return self.sm

    def trans(self, instance):
        self.screen_number = (self.screen_number + 1) % len(self.screens)
        self.sm.current = self.screens[self.screen_number].name


if __name__ == '__main__':
    TestApp().run()
'''

with open('structure.kv', encoding='utf8') as f:
    Builder.load_string(f.read())


class MainScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class QuestChooseScreen(Screen):
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
