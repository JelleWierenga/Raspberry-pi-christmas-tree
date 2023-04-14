import time
from rgbtree import RGBTree

tree = RGBTree()

while True:
    for i in range(24):
        tree.clear()
        tree.set_pixel(i, (255, 255, 255))
        tree.show()
        time.sleep(0.1)
