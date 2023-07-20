# Split out mandel as a function so we can call it if need be.
function mandel(;xmin=-2.0, xmax=1.0, ymin=-1.0, ymax=1.0, max_iter=25, xres=3072, yres=2048)
  rmax = 2.0
  pixels = zeros(Int64, xres, yres)
  for px = 1:xres
    x0 = (Float64(px)/Float64(xres)) * Float64(xmax - xmin) + xmin
    for py = 1:yres
      y0 = (Float64(py)/Float64(yres)) * Float64(ymax - ymin) + ymin
      iter = 0
      c = x0 + y0*im
      z = 0 + 0im
      while ((abs(z) < rmax) && (iter < max_iter)) 
        z = (z^2) + c
        iter = iter + 1
      end
      pixels[px,1+(yres-py)] = max_iter - iter
    end
  end

  return pixels
end

function julia(;xmin=-1.5, xmax=1.5, ymin=-1.5, ymax=1.5, n=2, c=-0.74543 + 0.11301im, max_iter=255, xres=3072, yres=3072)
  rmax = 2.0
  pixels = zeros(Int64, xres, yres)
  for px = 1:xres
    x0 = (Float64(px)/Float64(xres)) * Float64(xmax - xmin) + xmin
    for py = 1:yres
      y0 = (Float64(py)/Float64(yres)) * Float64(ymax - ymin) + ymin
      iter = 0
      z = x0 + y0*im
      while ((abs(z) < rmax) && (iter < max_iter)) 
        z = (z^n) + c
        iter = iter + 1
      end
      pixels[px,1+(yres-py)] = max_iter - iter
    end
  end

  return pixels
end

function convert_image(pixels; depth, width=72)
  stride = ceil(Int,size(pixels)[1]/width)
  corrected = pixels[1:stride:end, 1:stride:end]/depth
  return corrected
end
