import cocos
from pyglet.window import key

class sprites(cocos.layer.ScrollableLayer):
    def __init__(self):
        super().__init__()

        spr=cocos.sprite.Sprite("res/ufo_head.png")
        spr.position=400,360
        spr.velocity=(0,0)

        spr.do(Mover())

        self.add(spr)

class spritess(cocos.layer.ScrollableLayer):
    def __init__(self):
        super().__init__()

        spr=cocos.sprite.Sprite("res/player.png")
        spr.position=640,360
        spr.velocity = (0, 0)

        spr.do(Movers())

        self.add(spr)


class BackgroundLayer(cocos.layer.ScrollableLayer):
    def __init__(self):
        super().__init__()
        bg=cocos.sprite.Sprite("res/background.jpg")

        bg.position=bg.width//2,bg.height//2
        self.px_width=bg.width
        self.px_height=bg.height

        self.add(bg)



class Mover(cocos.actions.Move):
    def step(self, dt, ):
        super().step(dt)
        vel_x=(keyboard[key.RIGHT]-keyboard[key.LEFT])*500
        vel_y=(keyboard[key.UP]-keyboard[key.DOWN])*500
        self.target.velocity=(vel_x,vel_y)
        scroller.set_focus(self.target.x,self.target.y)

class Movers(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        vel_x=(keyboard[key.A]-keyboard[key.D]) *500
        vel_y=(keyboard[key.W]-keyboard[key.S])*500
        self.target.velocity = (vel_x, vel_y)
        scroller.set_focus(self.target.x,self.target.y)


if __name__=="__main__":
    cocos.director.director.init(width=1280,height=720,caption="keiki")
    cocos.director.director.window.pop_handlers()
    keyboard = key.KeyStateHandler()
    cocos.director.director.window.push_handlers(keyboard)
    sprites_layer=sprites()
    spritess_layer = spritess()

    bg_layer=BackgroundLayer()

    scroller=cocos.layer.ScrollingManager()
    scroller.add(bg_layer)
    scroller.add(spritess_layer)
    scroller.add(sprites_layer)

    test_scene=cocos.scene.Scene()
    test_scene.add(scroller)

    cocos.director.director.run(test_scene)