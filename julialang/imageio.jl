# This module provides routines for writing PGM/PBM images in Julia
# Owain Kenway

module imageio

export writepgm, writepbm

# Function for writing a PGM image.
# d is the pixel value array.
# white is the max vale which corresponds to white.
# filename is the file to write to.
function writepgm(d::Array{Int64,2}, white::Int64, filename::AbstractString)

  x = size(d, 1)
  y = size(d, 2)

  f = open(filename, "w")

# Write header
  write(f, "P2\n")
  write(f, "# Written by pnmmodules (https://github.com/owainkenwayucl/pnmmodules).\n")
  write(f, "$(x) $(y)\n")
  write(f, "$(white)\n") 

  for j = 1:y
    for i = 1:x
      write(f, "$(d[i,j])\n")
    end
  end

  close(f)

end

# Function for writing a PBM image.
# d is the pixel value array.
# threshold is the value at which 0 becomes 1
# filename is the file to write to.
function writepbm(d::Array{Int64,2}, threshold::Float64, filename::AbstractString)

  x = size(d, 1)
  y = size(d, 2)

  f = open(filename, "w")

# Write header
  write(f, "P1\n")
  write(f, "# Written by pnmmodules (https://github.com/owainkenwayucl/pnmmodules).\n")
  write(f, "$(x) $(y)\n")

  for j = 1:y
    for i = 1:x
      if Float64(d[i,j]) >= threshold 
        write(f, "1\n")
      else
        write(f, "0\n")
      end      
    end
  end

  close(f)

end

end
