import os
from os.path import join

import cv2

from tqdm import tqdm

import numpy as np
import random

from constants import *

path = os.getcwd()

data_file_path = join(join(path, ".."), 'Data Files')

dataset_path_training = join(data_file_path,'train')
dataset_path_testing = join(data_file_path,'valid')


def prepare_train_dataset(given_data_set_path):
    """
    This is used to prepare the data set for training
    """
    training_img = []
    training_label = []
     
    #lists for validation dataset
    valid_img = []
    valid_label = []
     
    folders = os.listdir(given_data_set_path)

    for folder in tqdm(folders):
        num_label = dict_diesease_num[folder]

        print("folder = {},\n label = {}".format(folder, num_label))
        images_path = os.path.join(given_data_set_path,folder)
     
        i =1 
        list_images = os.listdir(images_path)
        for image in tqdm(list_images):
            image_path=os.path.join(images_path,image)

            # read input image and convert into gray scale image
            img = cv2.imread(image_path)

            # Resize the image
            img = cv2.resize(img,(128,128))
            
            # get the number from the image
            number = str(num_label)
            
            # compute maximum length of the text
            max_label_len = 1
                
            
            # split the  validation and training dataset as 10% and 90% respectively
            if i%10 == 0: 
                valid_img.append(img)
                valid_label.append([(int(number))])
            else:
                training_img.append(img)
                training_label.append([int(number)]) 
            
            i+=1

    shuffle_testing = list(zip(training_img,
                               training_label))

    random.shuffle(shuffle_testing)

    training_img,training_label = zip(*shuffle_testing)

    np.save(join(data_file_path, 'valid_img.npy'),
        valid_img)
    np.save(join(data_file_path, 'valid_label.npy'),
        valid_label)

    np.save(join(data_file_path, 'training_img.npy'),
        training_img)
    np.save(join(data_file_path, 'training_label.npy'),
        training_label)
        
    return True


if __name__ == '__main__':
    result = prepare_train_dataset(dataset_path_training)


    

