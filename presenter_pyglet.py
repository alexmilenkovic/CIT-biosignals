import pyglet
from pyglet.gl import *

key = pyglet.window.key
#figbg = "test.jpg"

class CustomSprite(pyglet.sprite.Sprite):
    def __init__(self, texture_file, x=0, y=0):
        ## Must load the texture as a image resource before initializing class:Sprite()
        self.texture = pyglet.image.load(texture_file)

        super(CustomSprite, self).__init__(self.texture)
        self.x = x
        self.y = y

    def _draw(self):
        self.draw()

class MainScreen(pyglet.window.Window):
    def __init__ (self):
        super(MainScreen, self).__init__(800, 600, fullscreen = False)
        self.x, self.y = 0, 0

        #self.bg = CustomSprite(figbg)
        self.sprites = []
        self.alive = 1

    def on_draw(self):
        self.render()

    def on_close(self):
        self.alive = 0

    def clear_sprites(self):
        try:
            self.clear()
            self.sprites.pop()
        except:
            pass

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE: # [ESC]
            self.alive = 0
        elif symbol == key.C:
            print('Rendering cat')
            self.clear_sprites()
            self.sprites.append(
                    CustomSprite('img/cat.png', x=10, y=10)
                               )
        elif symbol == key.D:
            print('Rendering dog')
            self.clear_sprites()
            self.sprites.append(
                    CustomSprite('img/dog.png', x=10, y=10)
                               )
        elif symbol == key.R:
            doc = pyglet.text.decode_html("Hello")

    def render(self):
        self.clear()
        #self.bg.draw()

        for sprite_obj in self.sprites:
            sprite_obj._draw()

        self.flip()

    def run(self):
        while self.alive == 1:
            self.render()

            # -----------> This is key <----------
            # This is what replaces pyglet.app.run()
            # but is required for the GUI to not freeze
            #
            event = self.dispatch_events()

x = MainScreen()
x.run()

