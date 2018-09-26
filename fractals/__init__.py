'''
   Tools for generating fractals.
   Owain Kenway, 2018
'''

import numpy;

MAX_ITERATIONS=1000

def mandel(c, max_iter=MAX_ITERATIONS):
    iterations = 0
    z = 0 + 0j
    while (((numpy.absolute(z)) < 2) and (iterations < max_iter)):
        z = (z**2) + c
        iterations = iterations + 1
    return iterations

def julia(z, c, n, max_iter=MAX_ITERATIONS):
    iterations = 0
    while (((numpy.absolute(z)) < 2) and (iterations < max_iter)):
        z = (z**n) + c
        iterations = iterations + 1
    return iterations

def generate_julia(c, n):
    return lambda z,m : julia(z, c, n, max_iter=m)

def generate_fractal(width, height, func, xmin=-2, xmax=1, ymin=-1, ymax=1, max_iter=MAX_ITERATIONS):
    image = numpy.zeros((width, height), dtype=numpy.int64)
    xvals = numpy.linspace(xmin, xmax, width)
    yvals = numpy.linspace(ymin, ymax, height)
    for py in range(height):
        for px in range(width):
            c = xvals[px] + (1j*yvals[py])
            image[px,height - py - 1] = func(c,max_iter)
    return image

def generate_greyscale_palette(levels):
    pallette = []
    for i in numpy.linspace(0,255,levels,dtype=int):
        shade = hex(i)[2:]
        if len(shade) == 1:
            shade='0' + shade
        colour = '#' + shade + shade + shade
        pallette.append(colour)
    return pallette    

def show_image(image, palette=None):
    import tkinter

    width = image.shape[0]
    height = image.shape[1]

    if (palette == None):
        palette = generate_greyscale_palette(numpy.amax(image) + 1)

    window = tkinter.Tk()
    window.title("Fractal Image")
    canvas = tkinter.Canvas(window, width=width, height=height)
    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH) 
    for py in range(height):
        for px in range(width):
            canvas.create_oval(px,py,px+1,(py+1),fill=palette[image[px,py]], outline=palette[image[px,py]])            
    window.mainloop()


