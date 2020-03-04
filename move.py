import cocos
import pyglet
from cocos.director import director
from pyglet.window import key


class Mover(cocos.actions.Move):
    def step(self, dt, ):
        super().step(dt)
        vel_x=(keyboard[key.RIGHT]-keyboard[key.LEFT])*500
        vel_y=(keyboard[key.UP]-keyboard[key.DOWN])*500
        self.target.velocity=(vel_x,vel_y)