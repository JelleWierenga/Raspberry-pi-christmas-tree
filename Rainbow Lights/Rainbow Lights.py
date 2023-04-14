import time
from rgbtree import RGBTree

tree = RGBTree()

while True:
    for i in range(24):
        color = tree.get_rainbow_color(i / 24.0)
        tree.set_pixel(i, color)
    tree.show()
    time.sleep(0.05)
