#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 02:54:58 2022

@author: yavar
"""


import numpy as np

import matplotlib.pyplot as plt

import matplotlib.cm as cm
from skimage.measure import regionprops, label



#  create array of 0, 1 with weight

asize=(20,20)
#total number 
totnum=asize[0]*asize[1]

p=0.45


ar1=np.random.choice([1,0], asize, p=[p, 1-p])


regions = label(ar1 > 0)


clusternum=np.max(regions)

# ratio of occupied
ratio=np.sum(ar1)/totnum

clusters=[]


print('Label\t# pixels')
for region in regionprops(regions):
    print(f"{region['label']}\t{region['area']}")

cmap = cm.get_cmap('PiYG', 11)    

plt.imshow(regions, vmin=1, cmap="Paired", rasterized=True), plt.colorbar()








