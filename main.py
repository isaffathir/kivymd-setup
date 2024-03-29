from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from screens.screens import *

class WindowManager(MDScreenManager):
    pass

class NamaProjek(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.wm = WindowManager()
        screens = [
            Base(name="base"),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == '__main__':
    NamaProjek().run()
