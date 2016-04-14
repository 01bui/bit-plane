import sys, os
from skimage import data, color, io
import matplotlib.pyplot as plt

def main(sourceFile, destFile):
  im = io.imread(data.data_dir + '/chelsea.png')
  im = color.rgb2gray(im)
  print im
  plt.imshow(im)

if __name__ == "__main__":
  main('C:/Users/Events/PycharmProjects/bit-plane/CloudyGoldenGate_grayscale.jpg', 'C:/Users/Events/PycharmProjects/bit-plane/CloudyGoldenGate_grayscale_out.jpg')