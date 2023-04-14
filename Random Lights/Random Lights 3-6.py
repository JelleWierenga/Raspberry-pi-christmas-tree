import time
import random
from rgbtree import RGBTree

tree = RGBTree()

while True:
    num_lights = random.randint(3, 6)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for i in range(num_lights):
        light_index = random.randint(0, 23)
        tree.set_pixel(light_index, color)
    tree.show()
    time.sleep(0.5)