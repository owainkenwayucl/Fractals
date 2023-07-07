'''
   Tools for generating fractals.
   This library outputs numpy arrays to terminal.
   Owain Kenway, 2023
'''

COLOURS=' ░▒▓█'
ASCII_COLOURS=' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

# 256 colour ANSI
_ansi_colour_numbers = [x + 231 + 1 for x in range(24)]
_ansi_colour_numbers.append(231)
ANSI_COLOURS=['\033[48;5;'+str(x)+'m \033[m' for x in _ansi_colour_numbers]

def show(data, colours=ANSI_COLOURS):
		height = data.shape[1]
		width = data.shape[0]
		num_colours=len(colours)
		for a in range(height):
				for b in range(width):
						v = data[b,a]
						quantised = int(v * (num_colours - 1))

# Protect against having colour values outside our range.
						if quantised < 0:
								quantised = 0
						if quantised >= num_colours - 1:
								quantised = num_colours - 1

						print(colours[quantised], end='')
				print('')
