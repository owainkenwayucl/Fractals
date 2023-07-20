# Render a Greyscale image using xterm 256color colours
# I did *try* to use Crayons.jl but that breaks in screen while this doesn't.
# Owain Kenway

module TermShow

	export render_greyscale_image, hires_render_greyscale_image

	# This function prints out a greyscale version of an image by generating
	# "pixels" which are two spaces "  " with the background colour set from
	# the 25 greys in the 256 colour terminal colour set.
	function render_greyscale_image(image)
		num_colours = 25 
		base_colour = 231
		colours_int = fill(base_colour, num_colours)
		pixels = fill(" ", num_colours)
		for a in 1:num_colours-1 # every colour except the last one
			colours_int[a] = base_colour + a
		end

		for a in 1:num_colours
       			pixels[a] = "\033[48;5:"*string(colours_int[a])*"m  \033[m"
		end

		dimensions = size(image)

		width = dimensions[1]
		height = dimensions[2]

		for y in 1:height
			for x in 1:width
				index = Int(floor(image[x,y] * (num_colours-1))) + 1
				print(pixels[index])
			end
			println("")
		end
	end

	# This function prints out a greyscale version of an image by generating
	# pairs of pixels out of the "▄" character, setting the forground and 
	# background colour set from the 25 greys in the 256 colour terminal set.
	function hires_render_greyscale_image(image)
		num_colours = 25 
		base_colour = 231
		colours_int = fill(base_colour, num_colours)
		pixels = fill(" ", num_colours)
		for a in 1:num_colours-1 # every colour except the last one
			colours_int[a] = base_colour + a
		end

		dimensions = size(image)

		width = dimensions[1]
		height = dimensions[2]


		# Simple case, even number of pixes high.
		for y in 1:height ÷ 2
			line = ""
			slice = image[1:width,((2*y)-1):(2*y)]
			for x in 1:width
				index1 = Int(floor(slice[x,1] * (num_colours-1))) + 1
				index2 = Int(floor(slice[x,2] * (num_colours-1))) + 1
				pixel = "\033[48;5:"*string(colours_int[index1])*"m\033[38;5:"*string(colours_int[index2])*"m▄\033[m"
				line = line*pixel
			end
			println(line)
		end

		# If we have an odd number, generate the last row.
		if height % 2 == 1
			line = ""
			slice = image[1:width,height:height]
			for x in 1:width
				index1 = Int(floor(slice[x,1] * (num_colours-1))) + 1
				pixel = "\033[38;5:"*string(colours_int[index1])*"m▀\033[m"
				line = line*pixel
			end
			println(line)
		end
	end

end
