# Face-Detection-using-DWT
This program detects if the input face-image is present in a group of images in a directory. The feature extraction is done using Discrete Wavelet Transform, and the ORL faces are used as database.

Some points to make sure before running the program:

1. Do not give the entire orl-faces as the input directory. There are many folders inside the orl_faces. Choose one of them.
2. While giving the path of the input/test image, and the path of the directory in the 'orl_faces', replace the backward-slash ('\') by a forward-slash ('/') for Windows.
3. Do not name the test/input image, and the directory by a number, such as '1.jpg' (for the image),
 and '1' (for the directory). Give alphanumeric names.
