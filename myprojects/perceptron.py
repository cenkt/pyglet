from pdb import line_prefix
import pyglet
import random
import math
import numpy as np


WIN_X = 400
WIN_Y = 400
NUM_OBJECTS = 50


def calc_answ(x):
    return x + 0.4


class Perceptron:
    def __init__(self, shape, l_rate):
        self.weights = np.random.uniform(-1, 1, shape)
        self.l_rate = l_rate

    def __repr__(self) -> str:
        return "P_wghts%s" % (self.weights)

    def w_a(self, inpt):
        inpt = np.array(inpt)
        return np.dot(self.weights, inpt)

    def guess(self, inpt):
        wa = self.w_a(inpt)
        return 1 if wa >= 0 else -1


class Canvas(pyglet.window.Window):
    def __init__(self, width, height, noo):
        super().__init__(width, height)
        self.number_of_obj = noo
        self.batch = pyglet.shapes.Batch()
        self.list_of_obj = []
        for i in range(noo):
            xi = np.random.uniform(0, WIN_X)
            print(xi)
            yi = np.random.uniform(0, WIN_Y)
            self.list_of_obj.append(Dot(xi, yi, 3, color=(200, 100, 100), batch=self.batch))

    def on_mouse_release(self, x, y, button, modifiers):
        return

    def create_planet(self):
        return

    def update(self, dt):
        for obj in self.list_of_obj:
            obj.move(dt)

    def on_draw(self):
        self.clear()
        self.batch.draw()


class Dot(pyglet.shapes.Circle):
    def __init__(self, x, y, radius, color, batch):
        pyglet.shapes.Circle.__init__(
            self,
            x=x,
            y=y,
            radius=radius,
            color=color,
            batch=batch,
        )
        self.answ = 1 if self.y > calc_answ(x) else -1
        self.color = color if self.answ == 1 else (200, 200, 200)

    def __repr__(self) -> str:
        return "Point %s, %s, %s" % (self.x, self.y, self.answ)


canvas = Canvas(WIN_X, WIN_Y, NUM_OBJECTS)
perc1 = Perceptron(2, 0.1)
print([i for i in canvas.list_of_obj])
ins = [-0.5, 0.9]
print(ins, perc1)
print(perc1.w_a(ins), perc1.guess(ins))


@canvas.event
def on_draw():
    canvas.clear()
    canvas.batch.draw()
    # canvas.line.draw()


pyglet.app.run()
