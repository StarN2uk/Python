import math
import random
 
from matplotlib import pyplot as plt
 
colors = ["#984b00", "#317c00"]
 
 
def random_tree(x, y, angle, length, order, total):
    if order > 0:
        x2 = x + (math.cos(math.radians(angle)) * length)
        y2 = y + (math.sin(math.radians(angle)) * length)
        color = colors[0 if order >= 3 else 1]
        plt.plot([x, x2], [y, y2], color)
 
        l_angle = random.uniform(0, 40)
        r_angle = random.uniform(0, 40)
        scaled = random.uniform(0.7, 0.9)
 
        random_tree(x2, y2, angle - l_angle, length * scaled, order - 1, total)
        random_tree(x2, y2, angle + r_angle, length * scaled, order - 1, total)
 
 
if __name__ == '__main__':
    order = 12
    random_tree(x=100, y=100,
               angle=90,
               length=70,
               order=order,
               total=order)
 
    plt.show()