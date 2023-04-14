import time
from rgbtree import RGBTree

tree = RGBTree()

while True:
    for i in range(0, 255):
        tree.set_color((i, i, i))
        time.sleep(0.01)
    for i in range(255, 0, -1):
        tree.set_color((i, i, i))
        time.sleep(0.01)