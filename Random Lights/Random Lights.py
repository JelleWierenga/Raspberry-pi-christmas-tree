import time
import random
from rgbtree import RGBTree

tree = RGBTree()

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tree.set_color((r, g, b))
    time.sleep(0.5)