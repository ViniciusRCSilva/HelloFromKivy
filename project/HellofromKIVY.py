from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class HellofromKIVY(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        #side margins are 40% and top + bottom margins are 30%
        self.window.size_hint = (0.6, 0.7)
        
        #centering position
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        #image widget
        self.window.add_widget(Image(source = "../logo.png"))

        #label widget
        self.greeting = Label(
                text="What's your name?",
                font_size = 18,
            )
        self.window.add_widget(self.greeting)

        #text input widget
        self.user = TextInput(
                multiline = False,
                            #pixels
                padding_y = (20, 20),
                            #(width, heigh)
                size_hint = (1, 0.5),
            )
        self.window.add_widget(self.user)

        #button widget
        self.button = Button(
                text="GREET",
                size_hint = (1, 0.5),
                bold = True,
                background_color = '#370387ff',
                background_normal = ''
            )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        if (self.user.text == ''):
            self.greeting.text = "Enter a name!"
        else:
            self.greeting.text = "Kivy says hello to " + self.user.text + "!"


HellofromKIVY().run()