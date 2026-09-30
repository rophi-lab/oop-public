"""
Exercise 17: Tkinter - Add a Goal

Goal:
    A small tkinter game already lets you move a blue square with the WASD
    keys. Add a red rectangular GOAL and detect when the player reaches it.

Why this exercise?
    This is a gentle introduction to GUI programming and the "game loop"
    pattern. Instead of running top to bottom once, a GUI program reacts to
    events (key presses) and repeatedly calls update() many times per second
    via root.after(). You practice creating canvas shapes and writing simple
    rectangle-overlap collision detection.

What is already done for you:
    - The window, canvas, and blue player rectangle are created.
    - key_pressed / key_released track which keys are held down.
    - update() moves the player and re-schedules itself ~60 times per second.

The two things you implement:
    - goal: create a red rectangle with canvas.create_rectangle(x1, y1, x2, y2,
      fill="red"). Place it somewhere away from the player's start.
    - is_colliding(obj1, obj2): use canvas.coords(obj) to get each shape's
      [x1, y1, x2, y2] and return True when the two rectangles overlap.

Rectangle overlap rule:
    Two rectangles A and B overlap when:
        A.x1 < B.x2 and A.x2 > B.x1 and A.y1 < B.y2 and A.y2 > B.y1

TODO:
    1. Create the red goal rectangle.
    2. Complete is_colliding() so "Goal reached!" prints once when they overlap.
"""

import tkinter as tk


def key_pressed(event):
    pressed_keys.add(event.keysym.lower())

def key_released(event):
    pressed_keys.discard(event.keysym.lower())

def update():
    dx = 0
    dy = 0
    speed = 5

    if "w" in pressed_keys:
        dy -= speed
    if "s" in pressed_keys:
        dy += speed
    if "a" in pressed_keys:
        dx -= speed
    if "d" in pressed_keys:
        dx += speed

    canvas.move(player, dx, dy)

    if is_colliding(player, goal):
        print("Goal reached!")
        return

    # Call update again after 16 milliseconds
    # About 60 frames per second
    root.after(16, update)


root = tk.Tk()
root.title("Continuous WASD Movement")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

player = canvas.create_rectangle(
    180, 130, 220, 170,
    fill="blue"
)

# TODO: add a red rectangle goal
goal = None

def is_colliding(obj1, obj2):
    # TODO: complete the collision checking logic
    return False

pressed_keys = set()

root.bind("<KeyPress>", key_pressed)
root.bind("<KeyRelease>", key_released)

update()

root.mainloop()