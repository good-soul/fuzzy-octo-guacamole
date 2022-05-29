csvData has 27455 train images and 7172 test images in the form of an array of 784 pixel values

imgData has the same information but converted to 28x28 grayscale images to enable models to train on whole images instead of lists of pixels.

Each sub-directory in ingData corresponds to each alphabet the images represent. For example sub-directory '0' has all images for 'A' and sub-directory '1' has all images for 'B' and so on.

Directories corresponding to J and Z are not present since those cannot be represented at still images in sign language.