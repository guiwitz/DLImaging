[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/guiwitz/DLImaging/blob/master)
# Deep Learning for imaging

The repository is a course on Deep Learning in imaging based on the PyTorch and PyTorch Lightning packages. The audience of the course should be familiar with Python as well as with concepts of Machine and Deep Learning.  The course takes a very practical approach, showing all the steps necessary to create, train and use a Deep Learning  Neural Network (NN), the goal being to better understand the requirements, problems and challenges one can face even when *just using* such a NN. The course builds incrementally:

1. First we demonstrate how to handle imaging data in general, how to transform them into PyTorch tensor and handle those. 
2. We show in detail the basic steps of building and training a NN and handling datasets in PyTorch.
3. We show how higher-level libraries such as PyTorch Lightning can simplify some of those steps and provide advantages such as simpler switching to GPU, logging etc.
4. We dive deeper in the specificities of NN for imaging, in particular convolutional networks, image augmentation, auto-encoders.
5. After having mostly used classifiers as examples, we explore an other important type of models: segmentation models and build the popular Unet architecture.

In order to simplify the course organisation we mainly use simple synthetic datasets. All notebooks however can be excecuted e.g. on Google Colab where GPUs are available allowing to use larger datasets. We therefore encourage course participants to re-use the material with datasets of their choice.

## Installation

The necessary packages can easily be installed locally using conda with the [environment.yml](binder/environment.yml) file to create an environment:

```
conda env create -f environment.yml
```

This environment can then be activated and Jupyter started with:

```
conda activate DLImaging
jupyter lab
```

## Datasets

You can find the simple demo datasets on [Zenodo](https://zenodo.org/record/4465181). The data are stored in a zip file that you can directly download with [this link](https://zenodo.org/record/4465181/files/data.zip?download=1). This zip file should be unzipped and put at the same level as the ```notebooks``` folder of this repository for paths to work properly.
