import pyglet
import numpy as np


WIN_X = 400
WIN_Y = 400
NUM_OBJECTS = 50
SLOPE = np.random.uniform(
    -1,
    1,
)
INTERCEPT = np.random.uniform(
    0,
    WIN_X,
)


def calc_line(x):
    return SLOPE * x + INTERCEPT


class Perceptron:
    def __init__(self, shape, l_rate):
        self.weights = np.random.uniform(-1, 1, shape)
        self.l_rate = l_rate
        self.line = pyglet.shapes.Line(0, 0, 0, 0, 2, batch=canvas.batch)

    def __repr__(self) -> str:
        return f"P_wghts {self.weights}"

    def activate(self, sum):
        if sum > 0:
            return 1
        return -1

    def update_line(self):
        self.line.x1 = x1
        self.line.x2 = WIN_X
        self.line.y1 = -self.weights[2] - self.weights[0] * self.line.x1 / self.weights[1]
        self.line.y2 = -self.weights[2] - self.weights[0] * self.line.x2 / self.weights[1]

    def feed_forward(self, position):
        sum = 0
        for i in range(len(self.weights)):
            sum += self.weights[i] * position[i]
        return self.activate(sum)

    def train(self, point):
        guess = self.feed_forward(point.wghts)
        error_i = point.answ - guess
        for i in range(len(self.weights)):
            self.weights[i] += self.l_rate * error_i * point.wghts[i]

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
        self.wghts = self.position + (1,)

    def __repr__(self) -> str:
        return f"Point {self.wghts}, {self.answ})"


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
            print(self.list_of_obj[-1])

    def update(self, dt, perceptron):
        for i in self.list_of_obj:
            perceptron.train(i)
        perceptron.update_line()
        print(perceptron)

    def on_draw(self):
        self.clear()
        self.batch.draw()


canvas = Canvas(WIN_X, WIN_Y, NUM_OBJECTS)
perceptron = Perceptron(3, 0.001)
# print(perc1)

x1 = 0
x2 = WIN_X
y1, y2 = calc_line(x1), calc_line(x2)
border_line = pyglet.shapes.Line(x1, y1, x2, y2, 2, batch=canvas.batch)


# @canvas.event
# def on_draw():
#     canvas.clear()
#     canvas.batch.draw()


# pyglet.clock.schedule(canvas.update)
pyglet.clock.schedule_interval(canvas.update, 1 / 2, perceptron)
pyglet.app.run()
