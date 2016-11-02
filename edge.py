import argparse
import cv2
import numpy as np
from matplotlib import pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("min", type=int)
parser.add_argument("max", type=int)

args = parser.parse_args()

img = cv2.imread(args.filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)

sigma = 0.33

v = np.median(blur)

edges = cv2.Canny(blur, args.min, args.max)
lower = int(max(0, (1.0 - sigma) * v))
upper = int(min(255, (1.0 + sigma) * v))
edges_1 = cv2.Canny(blur, lower, upper)

cv2.imshow("Original", img)
cv2.imshow("Edges", np.hstack([edges, edges_1]))
cv2.waitKey(0)
