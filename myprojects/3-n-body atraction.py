# Accelerate to Mouse
import pyglet
import random
import math

# import numpy as np

win_x = 1100
win_y = 900
num_objects = 10
speed_range = 1
speed_mag_limit = 10
acc_range = 0
acc_mag_limit = 0.05
lim_mass = 3


def magnitute_v(vec_x, vec_y):
    return math.sqrt(vec_x**2 + vec_y**2)


def normalize_v(vec_x, vec_y):
    m = magnitute_v(vec_x, vec_y)
    return vec_x / m, vec_y / m


def subtract_v(mvx, mvy, vx, vy):
    return mvx - vx, mvy - vy


class Space(pyglet.window.Window):
    def __init__(self, width, height, noo):
        super().__init__(width, height)
        self.number_of_obj = noo
        self.gravity = 9.8
        self.batch = pyglet.shapes.Batch()
        self.list_of_obj = []
        self.mx = 0
        self.my = 0

        for i in range(self.number_of_obj):
            self.list_of_obj.append(self.create_planet())

    def on_mouse_motion(self, x, y, dx, dy):
        # print(x, y)
        self.mx = x
        self.my = y

    def create_planet(self):
        ox, oy = random.uniform(5, self.width), random.uniform(5, self.height)
        omass = random.uniform(5, lim_mass)
        odx, ody = random.uniform(-speed_range, speed_range), random.uniform(
            -speed_range, speed_range
        )
        oddx, oddy = random.uniform(-acc_range, acc_range), random.uniform(-acc_range, acc_range)
        ocolor = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        return Planet(
            x=ox,
            y=oy,
            radius=omass,
            dx=odx,
            dy=ody,
            ddx=oddx,
            ddy=oddy,
            color=ocolor,
            batch=self.batch,
        )

    def update(self, dt):
        for planet in self.list_of_obj:
            planet.move(dt)

    def on_draw(self):
        self.clear()
        self.batch.draw()


class Planet(pyglet.shapes.Circle):
    def __init__(self, x, y, radius, dx, dy, ddx, ddy, color, batch):
        super().__init__(
            x,
            y,
            radius,
            color=color,
            batch=batch,
        )
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ddx = ddx
        self.ddy = ddy
        self.mass = radius

    def calculate_acc(self, mx, my, dx, dy):
        return normalize_v(*subtract_v(mx, my, dx, dy))

    def move(self, dt):
        self.ddx, self.ddy = self.calculate_acc(space.mx, space.my, self.x, self.y)
        self.dx += self.ddx * acc_mag_limit
        self.dy += self.ddy * acc_mag_limit
        if magnitute_v(self.dx, self.dy) > speed_mag_limit:
            self.dx, self.dy = [speed_mag_limit * x for x in normalize_v(self.dx, self.dy)]
        self.x += self.dx
        self.y += self.dy


space = Space(win_x, win_y, num_objects)
pyglet.clock.schedule(space.update)
pyglet.app.run(interval=1/120)
