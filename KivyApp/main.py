from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest

class TutorialApp(App):
    def build(self):
        b = BoxLayout()

        f = FloatLayout()
        s = Scatter()





        self.request()
        self.l = Label(text='text',
                  font_size=15)
        f.add_widget(s)
        s.add_widget(self.l)

        b.add_widget(f)
        return b

    def request(self):
        req = UrlRequest(
            'http://127.0.0.1:8000/shop/8/3/',
            self.store_data)

    def store_data(self, reqest, results):
        print(results)




if __name__ == "__main__":
    TutorialApp().run()