import argparse
import cv2
import numpy as np
from matplotlib import pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("min", type=int)
parser.add_argument("max", type=int)

args = parser.parse_args()

img = cv2.imread(args.filename, 0)
edges = cv2.Canny(img, args.min, args.max)

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])

plt.show()
