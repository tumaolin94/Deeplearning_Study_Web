import matplotlib as mpl
mpl.use('Agg')    # for backend without gui
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
def load_data(host,save_path):

    file1 = host+'/logic/static/datasets/train_catvnoncat.h5'
    file2 = host+'/logic/static/datasets/test_catvnoncat.h5'
    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset(file1, file2)

    # Example of a picture
    index = 25
    plt.imshow(train_set_x_orig[index])
    plt.draw()
    plt.savefig(save_path+"/0.png")
    ## notice it will block, until you close the image window manually
    # plt.show()
def test():
    return 'Hello World'
