# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 07:17:49 2021

@author: DELL
"""
import os
from os.path import join

import numpy as np

import cv2

from keras.models import load_model

from constants import *

path = os.getcwd()

input_folder = join(join(path, 'static'),
                    'input_images')
model_weight_path = join(join(path,'model_files'),
                         'cnn_model.hdf5')

classifierLoad = load_model(model_weight_path)


def recognize_diesease():
    '''
    '''
    image_path = join(input_folder, 'leaf_image.jpg')
    input_image = cv2.imread(image_path)

    image = cv2.resize(input_image,(128,128))
    img = image.reshape(1,128,128,3)

    model_out = classifierLoad.predict(img)
    p = np.argmax(model_out)
    return dict_num_diesease[p]
        








    



    