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
        self.widget = Label(
                text="LOGIN",
                font_size = 18,
            )
        self.window.add_widget(self.widget)

        #label widget
        self.widget = Label(
                text="Name",
                font_size = 16,
            )
        self.window.add_widget(self.widget)

        #text input widget
        self.userName = TextInput(
                background_color = "#bfbfbf",
                background_active="#ffffff",
                multiline = False,
                            #pixels
                padding_y = (20, 20),
                            #(width, heigh)
                size_hint = (1, 1),
            )
        self.window.add_widget(self.userName)

        #label widget
        self.widget = Label(
                text="Password",
                font_size = 16,
            )
        self.window.add_widget(self.widget)

        #text input widget
        self.userPassword = TextInput(
                background_color = "#bfbfbf",
                background_active="#ffffff",
                password=True,
                multiline = False,
                            #pixels
                padding_y = (20, 20),
                            #(width, heigh)
                size_hint = (1, 1),
            )
        self.window.add_widget(self.userPassword)

        #label widget
        self.greeting = Label(
                text="",
                font_size = 18,
            )
        self.window.add_widget(self.greeting)

        #button widget
        self.button = Button(
                text="SIGN IN",
                size_hint = (1, 0.5),
                bold = True,
                background_color = '#370387ff',
                background_normal = ''
            )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        if (self.userName.text == '' or self.userPassword.text == ''):
            self.greeting.text = "Enter a name or password!"
        else:
            self.greeting.text = "Welcome " + self.userName.text + "!"


HellofromKIVY().run()