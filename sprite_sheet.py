import cocos
import pyglet

class snowman(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        img=pyglet.image.load("animation/cat_run.png")
        img_grid=pyglet.image.ImageGrid(img,1,16,item_width=90,item_height=190)
        anim=pyglet.image.Animation.from_image_sequence(img_grid[0:],0.1,loop=True)
        spr=cocos.sprite.Sprite(anim)
        spr.position=400,600
        self.add(spr)

if __name__=="__main__":
    cocos.director.director.init(width=1280,height=720,caption="keiki")
    cocos.director.director.window.pop_handlers()

    snowman_layer=snowman()

    test_scene=cocos.scene.Scene()
    test_scene.add(snowman_layer,0)

    cocos.director.director.run(test_scene)