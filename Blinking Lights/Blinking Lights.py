import time
from rgbtree import RGBTree

tree = RGBTree()

while True:
    tree.set_color((255, 0, 0))
    time.sleep(0.5)
    tree.set_color((0, 255, 0))
    time.sleep(0.5)