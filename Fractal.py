#!/usr/bin/env python3

# General fractal program

def _main():
	import argparse
	import fractals
	import sys

	parser = argparse.ArgumentParser(description="General Fractal Tool.")

# General options
	parser.add_argument("-W", "--width", metavar="width", type=int, help="Width.", default=600)
	parser.add_argument("-H", "--height", metavar="height", type=int, help="Height.", default=400)
	parser.add_argument("-x", "--xmin", metavar="xmin", type=float, help="Minimum value for X.", default=-2)
	parser.add_argument("-y", "--ymin", metavar="ymin", type=float, help="Minimum value for Y.", default=-1)
	parser.add_argument("-X", "--xmax", metavar="xmax", type=float, help="Maximum value for X.", default=1)
	parser.add_argument("-Y", "--ymax", metavar="ymax", type=float, help="Maximum value for Y.", default=1)
	parser.add_argument("-i", "--iters", metavar="iters", type=int, help="Maximum number of iterations.", default=50)

# Function select
	parser.add_argument("-f", "--func", metavar="func", type=str, help="Fractal function - valid options are mandelbrot, julia.", default="mandelbrot", choices=["mandelbrot", "julia"])

# Output options
	parser.add_argument("-d", "--display", metavar="display", type=str, help="Output style - valid options are tk, mpl, file.", default="tk", choices=["tk", "mpl", "file"])

	parser.add_argument("-o", "--output", metavar="filename", type=str, help="Output file name.", default="output.pgm")

# Julia only options
	parser.add_argument("-n", metavar="julia_n", type=int, help="Julia parameter N.", default=2)
	parser.add_argument("-z", metavar="julia_z", type=float, help="Julia parameter Z.", default=0.279)

# MPL only options
	parser.add_argument("-c", "--colourmap", metavar="colourmap", type=str, default="binary_r")

	args = parser.parse_args()

	image = ("",0)
	if args.func == "mandelbrot":
		image = fractals.generate_fractal(args.width, args.height, fractals.mandel, xmin=args.xmin, xmax=args.xmax, ymin=args.ymin, ymax=args.ymax, max_iter=args.iters)
	elif args.func == "julia":
		j = fractals.generate_julia(args.julia_z, args.julia_n)
		image = fractals.generate_fractal(args.width, args.height, j, xmin=args.xmin, xmax=args.xmax, ymin=args.ymin, ymax=args.ymax, max_iter=args.iters)
		
	else:
		sys.exit(1)


	if args.display == "tk":
		fractals.show_image(image)
	elif args.display == "mpl":
		fractals.show_image_matplotlib(image, palette=args.colourmap)
	elif args.display == "file":
		fractals.write_image(image, filename=args.output)
	elif args.display == "mplfile":
		fractals.write_image_matplotlib(image, palette=args.colourmap, filename=args.output)
	else:
		sys.exit(2)

if __name__ == "__main__":
	_main()
