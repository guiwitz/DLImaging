from skimage.draw import random_shapes
import skimage.transform
import numpy as np
import torch
from torch.utils.data import Dataset


def make_image(shape, imsize=32):
    """Generate image of given shape scaled 0-1.
    shape: str
        shape to draw (circle, triangle, rectangle)
    imsize: int
        size of image
    """
    
    image, _ = random_shapes((imsize,imsize),max_shapes=1, min_shapes=1, multichannel=False, shape=shape,
                                min_size=8)
    #normalize
    image = (255-image)/255

    # turn into tensor
    image_tensor = torch.tensor(image,dtype=torch.float32)
    
    return image_tensor


def make_image_rot(shape, angle, imsize=32):
    """Generate image of given shape scaled 0-1.
    shape: str
        shape to draw (circle, triangle, rectangle)
    imsize: int
        size of image
    """
    
    image, _ = random_shapes((imsize,imsize),max_shapes=1, min_shapes=1, multichannel=False, shape=shape,
                                min_size=8)
    #normalize
    image = (255-image)/255
    
    #rotate
    image = skimage.transform.rotate(image, angle, preserve_range=True)

    # turn into tensor
    image_tensor = torch.tensor(image,dtype=torch.float32)
    
    return image_tensor


class Drawings(Dataset):
    """Dataset class for quickdraw. Inputs are arrays of linearized 
    images and arrays of labels."""
    def __init__(self, data, targets, transform=None):
        self.data = data
        self.targets = torch.LongTensor(targets)
        self.transform = transform

    def __getitem__(self, index):
        x = self.data[index]
        x = np.reshape(x, (28,28))
        y = self.targets[index]

        if self.transform:
            x = self.transform(x)

        return x, y

    def __len__(self):
        return len(self.targets)