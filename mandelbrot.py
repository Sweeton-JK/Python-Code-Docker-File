import numpy as np
import matplotlib.pyplot as plt

def plot_mandelbrot_set(xmin, xmax, ymin, ymax, width, height):
  """Plots the Mandelbrot set to a given image."""
  c = np.zeros((width, height), dtype=complex)
  for i in range(width):
    for j in range(height):
      c[i, j] = complex(xmin + i * (xmax - xmin) / width, ymin + j * (ymax - ymin) / height)

  z = np.zeros((width, height), dtype=complex)
  for i in range(100):
    z = z * z + c

  plt.imshow(np.abs(z), cmap="hot")
  plt.colorbar()
  plt.show()

if __name__ == "__main__":
  plot_mandelbrot_set(-2.5, 1.5, -2.0, 2.0, 500, 500)