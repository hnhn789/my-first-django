from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import RiseInTransition 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
import select, socket, sys
from kivy.network.urlrequest import UrlRequest

def get():
	pass

class Screen_Manager(ScreenManager):
	background_image = ObjectProperty(Image(source='screen.png'))

class ChatApp(App):
	def build(self):
		self.sm = Screen_Manager()
		return self.sm


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = get_color_from_hex('#000000')

    ChatApp().run()