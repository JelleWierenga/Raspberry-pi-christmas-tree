import time
from rgbtree import RGBTree

tree = RGBTree()

while True:
    for i in range(24):
        tree.clear()
        color = (255, 255, 255)
        if i % 2 == 0:
            color = (255, 0, 0)
        tree.set_pixel(i, color)
        if i > 0:
            tree.set_pixel(i - 1, (0, 0, 255))
        if i < 23:
            tree.set_pixel(i + 1, (0, 0, 255))
        tree.show()
        time.sleep(0.1)
