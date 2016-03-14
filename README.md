# One-time Image
Convert a black and white image into two seemingly-random clouds of black and white pixels. Individually, each image can be mathematically proven to convey no data about the underlying image (assuming a good source of randomness was used), but print the images onto transparencies and overlay them and voila: the original image is revealed.

Designed to demonstrate how one-time pads work in a visual fashion.

# Requirements
Requires Python 2

Requires Python Imaging Library (http://www.pythonware.com/products/pil/)
* install with pip: *pip install pil*
* install with easy install: *easy_install pil*

# Running
Run *python one_time_image.py &lt;input_image&gt;*


Will produce two output files, *&lt;input imagename&gt;_1.png* and *&lt;input imagename&gt;_2.png*, in the same location as the source image.
