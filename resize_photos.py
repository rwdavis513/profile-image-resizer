
# coding: utf-8

# In[ ]:
import argparse
import os, sys
import skimage
from skimage import io
from skimage.transform import resize
#get_ipython().magic('matplotlib inline')


# In[10]:



# In[18]:

def load_image(file_name):
    img = io.imread(file_name)
    return img, img.shape
#img, size = load_image(os.path.join(img_dir, file_list[0]))


# In[29]:

def calc_new_size(size_array):
    width = size_array[1]
    height = size_array[0]
    ratio = height/width
    if ratio > 1.33:
        new_height = round(1.33*width)
        new_width = width
    elif ratio < 1.33:
        new_width = round(height/1.33)
        new_height = height
    return new_height, new_width
#calc_new_size(size)


def crop_image(img, new_size):
    return img[:new_size[0], :new_size[1]]
#io.imshow(crop_image(img, calc_new_size(img.shape)))

def process_images(img_dir, file_list):
    for file_name in file_list:
        print("Resizing image {}".format(file_name))
        img, size = load_image(os.path.join(img_dir, file_name))
        io.imsave(os.path.join(img_dir, os.path.splitext(file_name)[0] + '_4-3.jpg'), crop_image(img, calc_new_size(img.shape)))


def process_images_from_folder(img_dir= '/home/bobdavis/Documents/Lulu Tree/resize_photos/images'):
    file_list = [file_name for file_name in os.listdir(img_dir) if file_name.endswith(".jpg") or file_name.endswith(".png")]
    print("Processing files at " + img_dir)
    process_images(img_dir, file_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path to folder of images.", default=".")
    args = parser.parse_args()
    path = args.path
    if not os.path.exists(path):
        raise FileNotFoundError("Error: Please submit a valid path as an argument. Path entered: {}".format(path))
    process_images_from_folder(path)



