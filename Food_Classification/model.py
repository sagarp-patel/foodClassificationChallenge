# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:58:18 2020

@author: sagar
This is where the model will be created
"""
import numpy as np
from keras.preprocessing.image import image
from keras.preprocessing.image import img_to_array
from keras.applications.resnet50 import preprocess_input
from keras.applications.image_net_utils import decode_predictions
import matplotlib.pyplot as pyplt