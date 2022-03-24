import pyglet
import numpy as np


WIN_X = 400
WIN_Y = 400
NUM_OBJECTS = 50
SLOPE = 0.4  # np.random.uniform(    -1,    1,)
INTERCEPT = 40  # np.random.uniform(    0,    WIN_X,)


def calc_line(x):
    return SLOPE * x + INTERCEPT


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
        self.answ = 1 if self.y > calc_line(x) else -1
        self.color = color if self.answ == 1 else (200, 200, 200)

    def __repr__(self) -> str:
        return "Point %s, %s, %s" % (self.x, self.y, self.answ)


class Canvas(pyglet.window.Window):
    def __init__(self, width, height, noo):
        super().__init__(width, height)
        self.number_of_obj = noo
        self.batch = pyglet.shapes.Batch()
        self.list_of_obj = []
        self.create_dots(noo)

    def on_mouse_release(self, x, y, button, modifiers):
        return

    def create_dots(self, noo):
        for i in range(noo):
            xi = np.random.uniform(0, WIN_X)
            yi = np.random.uniform(0, WIN_Y)
            self.list_of_obj.append(Dot(xi, yi, 3, color=(200, 100, 100), batch=self.batch))

    def update(self, dt):
        # for obj in self.list_of_obj:
        #     obj.move(dt)
        pass

    def on_draw(self):
        self.clear()
        self.batch.draw()


canvas = Canvas(WIN_X, WIN_Y, NUM_OBJECTS)
perc1 = Perceptron(2, 0.1)

x1 = 0
x2 = WIN_X
y1, y2 = calc_line(x1), calc_line(x2)
border_line = pyglet.shapes.Line(x1, y1, x2, y2, 2, batch=canvas.batch)


# @canvas.event
# def on_draw():
#     canvas.clear()
#     canvas.batch.draw()


pyglet.clock.schedule(canvas.update)
pyglet.app.run()
