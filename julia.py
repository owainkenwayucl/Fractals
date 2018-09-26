import fractals

j = fractals.generate_julia(0.279,2)
fractals.show_image(fractals.generate_fractal(600,600, j, max_iter=50, xmin=-2.0, xmax=2.0, ymin=-2.0, ymax=2.0))
