'''
   Tools for generating fractals.
   Owain Kenway, 2018
'''

import numpy;

MAX_ITERATIONS=1000

# Function for Mandelbrot sets.
def mandel(c, max_iter=MAX_ITERATIONS):
    iterations = 0
    z = 0 + 0j
    while (((numpy.absolute(z)) < 2) and (iterations < max_iter)):
        z = (z**2) + c
        iterations = iterations + 1
    return iterations

# Generic function template for Julia sets.
def julia(z, c, n, max_iter=MAX_ITERATIONS):
    iterations = 0
    while (((numpy.absolute(z)) < 2) and (iterations < max_iter)):
        z = (z**n) + c
        iterations = iterations + 1
    return iterations

# Generator function for Julia set functions from given c, n.
def generate_julia(c, n):
    return lambda z,m : julia(z, c, n, max_iter=m)

# Generate an image (numpy array) of iterations for a given size, function, range, and maximum iterations.
def generate_fractal(width, height, func, xmin=-2, xmax=1, ymin=-1, ymax=1, max_iter=MAX_ITERATIONS):
    image = numpy.zeros((width, height), dtype=numpy.int64)
    ret_val = {}
    xvals = numpy.linspace(xmin, xmax, width)
    yvals = numpy.linspace(ymin, ymax, height)
    for py in range(height):
        for px in range(width):
            c = xvals[px] + (1j*yvals[py])
            image[px,height - py - 1] = func(c,max_iter)
    ret_val['image'] = image
    ret_val['depth'] = max_iter
    return ret_val

# generate a greyscale palette of colours for a given number of levels.
def generate_greyscale_palette(levels):
    palette = []
    for i in numpy.linspace(0,255,levels,dtype=int):
        shade = hex(i)[2:]
        if len(shade) == 1:
            shade='0' + shade
        colour = '#' + shade + shade + shade
        palette.append(colour)
    return palette    

# Show a tkinter window containing a given image.
def show_image(image_data, palette=None):
    import tkinter

    image = image_data['image']
    width = image.shape[0]
    height = image.shape[1]

    if (palette == None):
        palette = generate_greyscale_palette(image_data['depth'] + 1)

    window = tkinter.Tk()
    window.title("Fractal Image")
    canvas = tkinter.Canvas(window, width=width, height=height)
    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH) 
    for py in range(height):
        for px in range(width):
            canvas.create_oval(px,py,px+1,(py+1),fill=palette[image[px,py]], outline=palette[image[px,py]])            
    window.mainloop()

# Plot our image with matplotlib
def show_image_matplotlib(image_data, palette=None):
    import matplotlib.pyplot

    image = numpy.flipud(numpy.rot90(image_data['image']))

    matplotlib.pyplot.axis('off')
    if palette == None:
        matplotlib.pyplot.imshow(image)
    else:
        matplotlib.pyplot.imshow(image, cmap=palette)
    matplotlib.pyplot.show()