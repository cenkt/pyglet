# Accelerate to Mouse
import pyglet
import random
import math


win_x = 400
win_y = 400
num_objects = 1
speed_range = 5
speed_mag_limit = 50
# acc_range = 0
# acc_mag_limit = 0.1
lim_mass = 300


class Vector:
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Vector(%s, %s)" % (self.x, self.y)

    def plus_v(self, vec):
        self.x += vec.x
        self.y += vec.y

    def minus_v(self, vec):
        self.x -= vec.x
        self.y -= vec.y

    def scalar_v(self, a):
        self.y *= a
        self.x *= a

    def magnitute_v(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize_v(self):
        m = self.magnitute_v()
        self.x = self.x / m
        self.y = self.y / m

    def copy(self):
        return Vector(self.x, self.y)


class Space(pyglet.window.Window):
    def __init__(self, width, height, noo):
        super().__init__(width, height)
        self.number_of_obj = noo
        self.gravity = Vector(0.1, -0.2)
        self.batch = pyglet.shapes.Batch()
        self.list_of_obj = []
        self.mouse = Vector(0, 0)

        for i in range(self.number_of_obj):
            self.list_of_obj.append(self.create_planet())

    # def on_mouse_motion(self, x, y, dx, dy):
    #     self.mouse = Vector(x, y)

    def create_planet(self):
        ox, oy = 200, 200
        omass = 256
        odx, ody = 0, 0
        oddx, oddy = 0, 0
        ocolor = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        return Planet(
            x=ox,
            y=oy,
            radius=math.sqrt(omass),
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


class Planet(pyglet.shapes.Circle, Vector):
    def __init__(self, x, y, radius, dx, dy, ddx, ddy, color, batch):
        pyglet.shapes.Circle.__init__(
            self,
            x=self.x,
            y=self.y,
            radius=radius,
            color=color,
            batch=batch,
        )
        Vector.__init__(self, x, y)

        self.speed = Vector(dx, dy)
        self.acc = Vector(ddx, ddy)
        self.mass = math.pow(self.radius, 2)
        self.trails = []

    def calculate_acc(self, vec):
        # temp = vec.copy()
        # temp.minus_v(self)
        # temp.normalize_v()
        self.acc = vec

    def check_edge(self):
        if (self.y) <= self.radius:
            self.y = self.radius
            self.speed.y = -self.speed.y

        if (self.y) >= space.height - self.radius:
            self.y = space.height - self.radius
            self.speed.y = -self.speed.y

        if (self.x) <= self.radius:
            self.x = self.radius
            self.speed.x = -self.speed.x

        if (self.x) >= space.width - self.radius:
            self.x = space.width - self.radius
            self.speed.x = -self.speed.x

    def move(self, dt):
        old_x, old_y = self.x, self.y
        self.calculate_acc(space.gravity)
        self.speed.plus_v(self.acc)
        self.plus_v(self.speed)
        self.check_edge()
        trail = pyglet.shapes.Line(self.x, self.y, old_x, old_y, 1, batch=space.batch)
        trail.opacity = 100
        self.trails.append(trail)


space = Space(win_x, win_y, num_objects)
pyglet.clock.schedule(space.update)
# pyglet.clock.schedule_interval(space.update, 1 / 2)
pyglet.app.run()
