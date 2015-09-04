import png
import sys
import itertools
import fileinput


WIDTH = 4096
HEIGHT = 4096


def calc_green(value):
    return round((50 - abs(50 - value)) * (255.0 / 50.0))

def calc_blue(value):
    return round(max(50 - value, 0) * (255.0 / 50.0))

def calc_red(value):
    return round(value * (255.0 / 100.0))

def calc_rgb(value):
    return calc_red(value), calc_green(value), calc_blue(value)

def gen_random_pixel():
    return calc_rgb(randint(0, 100))

def gen_random_row(length):
    return map(int, itertools.chain(*
        map(lambda i: calc_rgb(i * (100.0 / WIDTH)), xrange(WIDTH))
    ))

def stdin_read_heatvalues():
    for line in fileinput.input():
        row = map(int, line.split())
        for value in row:
            yield value

def parse_heatvalues():
    array = []
    iter_heatvalues = stdin_read_heatvalues()
    for row_i in xrange(HEIGHT):
        array.append([])
        for col_j in xrange(WIDTH):
            array[row_i].extend(calc_rgb(iter_heatvalues.next()))
    return array


# Example gradient heatmap:
with open('example_heatmap.png', 'wb') as f:
    w = png.Writer(WIDTH, HEIGHT)

    w.write(f, parse_heatvalues())
