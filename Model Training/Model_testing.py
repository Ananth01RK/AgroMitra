import cv2
from keras.models import load_model

import numpy as np

from Constants import dict_num_diesease

classifierLoad = load_model('.//..//Data Files//CNN_MODEL.h5')
print(classifierLoad)


def recognize_character(image):
    '''
    '''
    image = cv2.resize(image,(64,64))
    img=image.reshape(1,64,64,1)
    model_out=classifierLoad.predict(img)
    p=np.argmax(model_out)
    return dict_num_diesease[p]


image = cv2.imread(".//..//Data Files//train//Bacterial_spot//0a22f50a-5f25-4cf6-816b-76cae94b7f30___GCREC_Bact.Sp 6103.jpg",0)
print(recognize_character(image))