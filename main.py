from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from screens.screens import *

class WindowManager(ScreenManager):
    pass

class NamaProjek(MDApp):
    CLASSES = {
        'Home':'screens.home',
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive': True})
    ]
    KV_FILES = [
        'kv/home.kv',
    ]
    def build_app(self):
        self.wm = WindowManager()
        screens = [
            Home(name="home"),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == '__main__':
    NamaProjek().run()