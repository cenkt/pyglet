import pyglet
import numpy as np


WIN_X = 750
WIN_Y = 750
NUM_OBJECTS = 500
SLOPE = np.random.uniform(
    -1,
    1,
)
INTERCEPT = np.random.uniform(
    -1,
    1,
)
X_MIN = -1
X_MAX = 1
Y_MIN = -1
Y_MAX = 1


def calc_line(x):
    return SLOPE * x + INTERCEPT


def renormalize(n, range1, range2):
    delta1 = range1[1] - range1[0]
    delta2 = range2[1] - range2[0]
    return (delta2 * (n - range1[0]) / delta1) + range2[0]


class Perceptron:
    def __init__(self, shape, l_rate):
        self.weights = np.random.uniform(-1, 1, shape)
        self.l_rate = l_rate
        self.line = pyglet.shapes.Line(0, 0, 0, 0, 1, batch=canvas.batch)

    def __repr__(self) -> str:
        return f"P_wghts {self.weights}"

    def activate(self, sum):
        if sum > 0:
            return 1
        return -1

    def update_line(self):
        dmx = X_MIN
        dmx2 = X_MAX
        dmy = (-self.weights[2] - self.weights[0] * dmx) / self.weights[1]
        dmy2 = (-self.weights[2] - self.weights[0] * dmx2) / self.weights[1]
        self.line.x = renormalize(dmx, (X_MIN, X_MAX), (0, WIN_X))
        self.line.x2 = renormalize(dmx2, (X_MIN, X_MAX), (0, WIN_X))
        self.line.y = renormalize(dmy, (Y_MIN, Y_MAX), (0, WIN_Y))
        self.line.y2 = renormalize(dmy2, (Y_MIN, Y_MAX), (0, WIN_Y))

    def feed_forward(self, position):
        sum = 0
        for i in range(len(self.weights)):
            sum += self.weights[i] * position[i]
        return self.activate(sum)

    def train(self, point):
        guess = self.feed_forward(point.coords)
        error_i = point.answ - guess
        for i in range(len(self.weights)):
            self.weights[i] += self.l_rate * error_i * point.coords[i]


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
        bx = renormalize(x, (0, WIN_X), (X_MIN, X_MAX))
        by = renormalize(y, (0, WIN_Y), (Y_MIN, Y_MAX))
        self.coords = (bx, by, 1)
        self.answ = -1 if by < calc_line(bx) else 1
        self.color = color if self.answ == 1 else (200, 200, 200)

    def __repr__(self) -> str:
        return f"Point {self.coords}, {self.answ})"


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

    def update(self, dt, perceptron):
        perceptron.update_line()
        for i in self.list_of_obj:
            perceptron.train(i)

    def on_draw(self):
        self.clear()
        self.batch.draw()


canvas = Canvas(WIN_X, WIN_Y, NUM_OBJECTS)
perceptron = Perceptron(3, 0.0001)

x = renormalize(X_MIN, (X_MIN, X_MAX), (0, WIN_X))
y = renormalize(calc_line(X_MIN), (Y_MIN, Y_MAX), (0, WIN_Y))
x2 = renormalize(X_MAX, (X_MIN, X_MAX), (0, WIN_X))
y2 = renormalize(calc_line(X_MAX), (Y_MIN, Y_MAX), (0, WIN_Y))
border_line = pyglet.shapes.Line(x, y, x2, y2, 3, batch=canvas.batch)


pyglet.clock.schedule_interval(canvas.update, 0.1, perceptron)
pyglet.app.run()
