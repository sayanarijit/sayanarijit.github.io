---
layout: note
tags:
  - tech
  - computer-science
  - book
  - learning
  - ai
---

# Fastbook

Notes from the [Fastbook][1].

### Chapter 1: Intro

- GPUs are capable of PDP (parallel distributed processing), an important ability necessary to train AI models mimicking the neural networks in our brain.
- As of now it's preferable to rent GPUs than to buy them because
  - Prices and specs are rapidly changing.
  - Hard to setup.
  - Hard to maintain.
- "Deep Learning" is the state of the art machine learning approach, usable in a wide range of applications.
- Two things can be learned by AI are - text and visual data.
- Many kinds of data (e.g. sound, temperature) can be represented as pictures, and thus be used by a visual learner.
- An "architecture" is the implementation of a deep leaning algorithm that can recognize patterns from the given set of inputs and outputs, and use them to predict outputs for future inputs, even unseen ones.
- A "model" is an instance of an architecture with parameters, i.e. an instance of an architecture that has learned things.
- "resnet34" is an example of a pre-trained model using the CNN (Convolutional Neural Network) architecture with 34 layers.
- While learning, the model goes through the training data, often multiple times, each time, storing the recognized patterns in its layers as values called "parameters" aka "weights".
- The last layer of a model, aka the "head", stores the most specialized parameters for the dataset it has been trained on.
- While training a pre-trained model, the parameters in the latter layers, specially the head is replaced with new parameters acquired from the new dataset.
- It's easier and faster to fine-tune, i.e. train a pre-trained model, than training one from scratch.
- Before training, the learner sets aside about 20% of the data for validation after the training.
- Use the same set of data for validation in all iterations to avoid bias.
- The error rate (percentage of incorrect predictions) should reduce after each epoch (iteration) of processing the dataset.
- Too much training on limited data can cause over-fitting, i.e. the model starts memorizing outputs for the given inputs, rather than predicting.
- Over-fitting will cause error rate to increase.
- There the two kinds of predictions: Classification and regression.
- Classification: given an input, predict the matching label as output from a given set of discrete labels (e.g. recognizing dogs vs cats).
- Regression: given a continuous series of inputs, predict the future trajectory of the series as output (e.g. predicting temperature changes).

```python
# Import all the useful utilities to train a visual learning model
from fastai.vision.all import *

# Download and extract dataset
path = untar_data(URLs.PETS)/'images'

# Function to process a filename and return the label
def is_cat(x):
  return x[0].isupper()

# A loader that can load data and label them by processing filenames
data_loaders = ImageDataLoaders.from_name_func(
  path,  # path to the dataset
  get_image_files(path),  # The input data.
  valid_pct=0.2,  # Set aside 20% for validation after training.
  seed=42,  # Use the same seed in each epoch to ensure same set of validation data is used.
  label_func=is_cat,  # Function to process labels from filename
  item_tfms=Resize(224),  # Resize the images to the same size for processing them efficiently in GPU.
)

# Use a CNN implementation with 34 layers
architecture = resnet34

# Use predefined function error_rate for validating and measuring the quality
metric = error_rate

# Initialize the vision learner model
learner = vision_learner(
  data_loaders,
  architecture,
  metrics=metrics,
)

# Fine-tune the pre-trained model in 1 epoch (iteration)
learner.fine_tune(1)
```

### Chapter 2: Production

- Use the [Drivetrain][3] approach to get better results.
- When training vision learning models, use Data Augmentation i.e. transform the training images by cropping, rotating, applying filters etc.
- Think about the possible biases in the dataset.
- Train a small model first, and use that to clean the data before training bigger models.
- Data cleaning can be done by plotting confusion metrics.
- Create notebook apps as POC first.
- To avoid disaster, do human checks, keep the scope limited, expand gradually.
- Be aware of positive feedback loops, where the model starts learning biases when data doesn't represent the intention.

### Chapter 3: MNIST basics

- MNIST is a popular dataset containing images of handwritten digits.
- We generally use the Image library from PIL to work on images, it's supported directly by Jupyter Notebook.
- numpy "array" and pytorch "tensor" are mathematical data structures that can store values of any dimension (digit, array of digits, array of array of digits...).
- They are almost similar, but tensor restricts its elements to be of the same type and shape, which lets it utilize the GPU and provide some other conveniences required for deep learning.
- Images can be stored in a tensor by dividing each pixel by 255.
- Image stored in a tensor can be shown in Jupyter notebook using the `show_image()` function.
- Multiple images can be stacked into a tensor using the `torch.stack()` function.
- The first axis of the stacked tensor is the indexes of the images.
- Get the mean image of all stacked images using the `.mean()` method.
- `.mean((-1,-2))` will take the mean ranging over the values indexed by the last two axes (horizontal, vertical) of the stacked tensor.
- Get the mean absolute value loss (L1 loss) (`(img1-img2).abs().mean()`) using the `F.l1_loss()` function.
- Get the mean squared error (MSE) (`((img1-img2)^2).mean().sqrt()`) using the `F.mse_loss()` function.
- These functions can be used to get the differences between two images.
- As compared to L1 loss, MSE is more strict towards large differences.
- "Gradient" in SGD is a measure of - for each weight, how changing that weight would change the loss.
-

[1]: https://github.com/fastai/fastbook
[2]: https://www.fast.ai
[3]: https://www.oreilly.com/radar/drivetrain-approach-data-products
