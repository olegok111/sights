# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import dbwrite

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')


def console_debug_output(instance):
    print('Element', instance.text, 'built succesfully.')


def exit_action(instance):
    exit(0)


def add_10(instance):
    prev_points = dbwrite.pget(instance.text)['points']
    dbwrite.pwrite(instance.text, prev_points+10)


class W2App(App):

    def build(self):
        b = Button(text='HEEEEEEY!')
        return b


class TestApp(App):

    def build(self):
        all_scr_lyt = FloatLayout()
        button_exit = Button(text='X', font_size=72, background_color=[1, 0, 0, 1], background_normal='',
                             pos=(680, 510), size_hint=(.15, .15), on_press=exit_action)
        main_btn_lyt = BoxLayout(orientation='vertical', padding=[120], spacing=40,
                                 pos=(0, 0), size_hint=(1, .85))
        btn_1 = Button(text='Продолжить', on_press=console_debug_output)
        btn_2 = Button(text='Сменить игрока', on_press=W2App().run)
        btn_3 = Button(text='nond', on_press=add_10)
        all_scr_lyt.add_widget(button_exit)
        main_btn_lyt.add_widget(btn_1)
        main_btn_lyt.add_widget(btn_2)
        main_btn_lyt.add_widget(btn_3)
        all_scr_lyt.add_widget(main_btn_lyt)
        return all_scr_lyt


if __name__ == '__main__':
    TestApp().run()