from ursina import *
from math import floor
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina(borderless=False)
window.size = (1200, 600)

size = 32

plane = Entity(
    model='quad',
    color=color.azure,
    z=10,
    collider='box',
    scale=size
)

grid = [[
    Entity(
        model='quad',
        collider='box',
        position=(x, y, -.1),
        texture='white_cube',
        enabled=False,
    )
    for y in range(size)]
    for x in range(size)]

player = PlatformerController2d()
player.position = (16, 20, -.1)
cursor = Entity(model=Quad(mode='line'), origin=(.5, .5), color=color.lime)

camera.orthographic = True
camera.fov = 15
camera.position = (16, 18, -50)

for column in grid:
    for e in column:
        if e.y <= 15:
            e.enabled = True

def input(key):
    pos = mouse.world_point
    if pos is not None:
        if key == 'left mouse down':
            grid[int(pos.x)][int(pos.y)].enabled = True
        if key == 'right mouse down':
            grid[int(pos.x)][int(pos.y)].enabled = False

app.run()