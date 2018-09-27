import fractals

# Generate julia sets as per https://en.wikipedia.org/wiki/Julia_set#Examples_of_Julia_sets

n = 2
c = [0.279, 0.400, 0.484, 0.544, 0.590, 0.626]
for i in c: 
    j = fractals.generate_julia(i,n)
    fractals.show_image_matplotlib(fractals.generate_fractal(600,600, j, max_iter=50, xmin=-2.0, xmax=2.0, ymin=-2.0, ymax=2.0))
    n += 1
