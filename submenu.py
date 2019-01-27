from gi.repository import Nautilus, GObject
from pynput.keyboard import Key, Controller

class ExampleMenuProvider(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def menu_background_activate_cb(self, menu, file):
        keyboard = Controller() 
        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        
    def get_background_items(self, window, file):
        menuitem = Nautilus.MenuItem(name='ExampleMenuProvider::Foo', 
                                         label='Foo', 
                                         tip='',
                                         icon='')
        menuitem.connect('activate', self.menu_background_activate_cb, file)
        return menuitem,

