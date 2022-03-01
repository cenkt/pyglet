import pyglet

# batch = pyglet.graphics.Batch()
# i = 10

# ball_image = pyglet.image.load("pyglet.png")
# # ball = pyglet.sprite.Sprite(ball_image, x=50, y=50)
# # sprites = [pyglet.sprite.Sprite(ball_image, x=50 + (i * 100), y=50, batch=batch) for i in range(10)]


# window = pyglet.window.Window(1500, 500)
# l = []


# def update(dt):
#     global i
#     l.append(pyglet.sprite.Sprite(ball_image, i, i, batch=batch))
#     print(i)
#     i += 100


# @window.event
# def on_draw():
#     batch.draw()
#     # return


# pyglet.clock.schedule_interval(update, 1)
# pyglet.app.run()

# print("Done")

# from pyglet import *

window = pyglet.window.Window(1000, 500, "App", resizable=True)
window.set_minimum_size(500, 250)


@window.event
def on_draw():
    window.clear()
    sprite.draw()


file = "pyglet.png"
image = pyglet.image.load(file)
sprite = pyglet.sprite.Sprite(image, x=20, y=20)

pyglet.app.run()
