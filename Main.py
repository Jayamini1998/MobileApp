from kivy.app import app
from kivy.uix.boxlayout import boxlayout
from kivy.uix.button import button
from kivy.uix.textinput import textinput

class MainApp(App):
    def build(self):
        self.operators = ["/","*","+","-"]

if __name__ == "__main__":
    app = MainApp()
    app.run()
