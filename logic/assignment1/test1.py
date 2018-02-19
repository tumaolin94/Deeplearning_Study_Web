import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from scipy import ndimage
from lr_utils import load_dataset
from IPython.display import display
from PIL import Image

# train_dataset = h5py.File('/static/datasets/train_catvnoncat.h5', "r")
# train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
def load_data(host):
    # Loading the data (cat/non-cat)
    # train_dataset = h5py.File(host+'/logic/static/datasets/train_catvnoncat.h5', "r")
    file1 = host+'/logic/static/datasets/train_catvnoncat.h5'
    file2 = host+'/logic/static/datasets/test_catvnoncat.h5'
    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset(file1, file2)

def test():
    return 'Hello World'
