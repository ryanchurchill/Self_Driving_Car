# Importing the Kivy packages
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.label import Label

class Car(Widget):
    angle = NumericProperty(0)

class Map(Widget):
    pass

class Ball(Widget):
    pass

class Form(Widget):
    pass
#     car = ObjectProperty(None)
#     print(car.center)


class SelfDrivingCarApp(App):

    def build(self):
        my_form = Form()
        return my_form
        # return Label(text='Hello world')
        # return Car()

if __name__ == '__main__':
    SelfDrivingCarApp().run()