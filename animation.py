import cocos
import pyglet

class sprites(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        img=pyglet.image.load("res/bomb_sprite.png")
        img_grid=pyglet.image.ImageGrid(img,1,15,item_width=100,item_height=100)
        anim=pyglet.image.Animation.from_image_sequence(img_grid[0:],0.1,loop=True)
        spr=cocos.sprite.Sprite(anim)
        spr.position=400,600
        self.add(spr)

class spritess(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        spr=cocos.sprite.Sprite("res/player.png")
        spr.position=640,360

        self.add(spr)


if __name__=="__main__":
    cocos.director.director.init(width=1280,height=720,caption="keiki")
    cocos.director.director.window.pop_handlers()

    sprites_layer=sprites()
    spritess_layer = spritess()

    test_scene=cocos.scene.Scene()
    test_scene.add(sprites_layer,0)
    test_scene.add(spritess_layer,1)

    cocos.director.director.run(test_scene)