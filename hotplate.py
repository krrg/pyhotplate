import png
import sys
import itertools


WIDTH = 128
HEIGHT = 128


def calc_green(value):
    return round((50 - abs(50 - value)) * (255.0 / 50.0))

def calc_blue(value):
    return round(max(50 - value, 0) * (255.0 / 50.0))

def calc_red(value):
    return round(max(value - 50, 0) * (255.0 / 50.0))

def calc_rgb(value):
    return calc_red(value), calc_green(value), calc_blue(value)

def gen_random_pixel():
    return calc_rgb(randint(0, 100))

def gen_random_row(length):
    return map(int, itertools.chain(*
        map(lambda i: calc_rgb(i * (100.0 / WIDTH)), xrange(WIDTH))
    ))

# Example gradient heatmap:
# with open('example_heatmap.png', 'wb') as f:
#     w = png.Writer(WIDTH, HEIGHT)
#     w.write(f, [gen_random_row(WIDTH)]*HEIGHT)
