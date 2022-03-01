import pyglet
import math

x = 500
y = 500
step_size = 20
max_size = x * y / (step_size**2)


class Letters(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.batch = pyglet.shapes.Batch()
        self.time = 0
        self.step = 1
        self.turncount = 1
        self.numstep = 1
        self.turn_angle = 0
        self.x = self.width / 2
        self.y = self.height / 2
        self.label_list = []

    def check_prime(self):
        if self.step == 1:
            return False
        for i in range(2, int(math.sqrt(self.step)) + 1):
            if self.step % i == 0:
                return False
        return True

    def update(self, dt):
        self.time += dt
        if self.check_prime():
            # self.label = pyglet.text.Label(
            #     str(self.step),
            #     font_name="Times New Roman",
            #     font_size=int(step_size * 0.7),
            #     anchor_x="center",
            #     anchor_y="center",
            #     # color=(100, 0, 200, 100),
            #     x=self.x,
            #     y=self.y,
            #     batch=self.batch,
            # )
            self.label_list.append(
                pyglet.shapes.Circle(
                    x=self.x, y=self.y, radius=step_size / 2, color=(100, 0, 200), batch=self.batch
                )
            )
        self.pos_update()
        self.step += 1
        if self.step > max_size:
            pyglet.clock.unschedule(letters.update)

    def pos_update(self):
        # print(self.step, self.numstep, self.turncount)
        if self.turn_angle == 0:
            self.x += step_size
        elif self.turn_angle == 1:
            self.y += step_size
        elif self.turn_angle == 2:
            self.x -= step_size
        elif self.turn_angle == 3:
            self.y -= step_size

        if self.step % self.numstep == 0:
            self.turn_angle = (self.turn_angle + 1) % 4
            self.turncount += 1
            if self.turncount % 2 == 0:
                self.numstep += 1

    def on_draw(self):
        self.clear()
        self.batch.draw()


letters = Letters(x, y)
pyglet.clock.schedule_interval(letters.update, 1 / 1000)
pyglet.app.run()
