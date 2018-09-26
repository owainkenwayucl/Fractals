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

def generate_fractal(width, height, func, xmin=-2, xmax=1, ymin=-1, ymax=1, max_iter=MAX_ITERATIONS):
    image = numpy.zeros((width, height), dtype=numpy.int64)
    xvals = numpy.linspace(xmin, xmax, width)
    yvals = numpy.linspace(ymin, ymax, height)
    for py in range(height):
        for px in range(width):
            c = xvals[px] + (1j*yvals[py])
            image[px,height - py - 1] = func(c,max_iter)
    return image

def show_image(image):
    import tkinter

    width = image.shape[0]
    height = image.shape[1]

    maxcolour = numpy.amax(image)

    window = tkinter.Tk()
    window.title("Fractal Image")
    canvas = tkinter.Canvas(window, width=width, height=height)
    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH) 
    for py in range(height):
        for px in range(width):
            shade = hex(int((float(image[px,py])/float(maxcolour)) * 256)-1)[2:]
            if len(shade) == 1:
                shade='0' + shade
            colour = '#' + shade + shade + shade
            canvas.create_oval(px,py,px+1,(py+1),fill=colour, outline=colour)            
    window.mainloop()


