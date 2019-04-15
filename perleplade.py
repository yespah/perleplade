__author__ = 'jesper'

import imageio
import numpy as np
import matplotlib.pyplot as plt


def pp_slice(image, pp_x, pp_y):
    pp = np.array((pp_x, pp_y, 3))
    img = imageio.imread(image)
    size = img.shape[:2]
    slice_x = round(size[0] / pp_x) - 1
    slice_y = round(size[1] / pp_y) - 1
    for i in range(0,pp_x-1):
        for j in range(0,pp_y-1):
            timg = img[i*slice_x:i*slice_x+slice_x, j*slice_y:j*slice_y+slice_y]
            pp[i,j] = [np.median(timg[0]),np.median(timg[1]),np.median(timg[2])]
    return pp

pp1 = pp_slice("Sofia.jpg", 19, 19)

plt.imshow(pp1)
