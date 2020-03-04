import cocos


class helloCocos(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        label=cocos.text.Label("hello cocos",font_name="Times New Roman",font_size=32,anchor_x="center",anchor_y="center")

        size=cocos.director.director.get_window_size()
        print(size)
        label.position=size[0]/2,size[1]/2
        self.add(label)


if __name__=="__main__":
    cocos.director.director.init(width=1280,height=720,caption="my cocos window")

    hello_layer=helloCocos()

    test_scene=cocos.scene.Scene(hello_layer)

    cocos.director.director.run(test_scene)