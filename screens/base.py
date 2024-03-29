from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import NumericProperty,StringProperty

Builder.load_file("screens/kv/base.kv")

class Base(MDScreen):
    label_text = StringProperty()
    def __init__(self, **kw):
        super().__init__(**kw)
        self.count = 0
        self.label_text = str(self.count)

    def tambah(self,*args):
        self.count += 1
        self.label_text = str(self.count)
    
    def kurang(self,*args):
        if self.count != 0:
            self.count -= 1
        elif self.count == 0:
            print("anti angka negatif")
        self.label_text = str(self.count)
        