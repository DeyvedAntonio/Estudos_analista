from kivy.app import App
from kivy.uix.label import Label


class Calculadora(App):
    def build(self):
        return Label(text='Calculadora')


Calculadora().run()
