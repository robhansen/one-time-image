
'''
Copyright (c) 2016, Robert Hansen
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

from PIL import Image
import PIL.ImageOps
import random
import sys

if len(sys.argv) != 2:
  print "Error: run 'python "+sys.argv[0]+" <input image>'"
  sys.exit()

# open input file
im = Image.open(sys.argv[1])
# convert to grayscale
im = im.convert('L') 
# force to black and white
im = im.convert('1', dither=Image.NONE)
# and back to greyscale
im = im.convert('L')

width, height = im.size
sourcePixels = im.getdata()

# create buffers for the output images (4 times the size of the original)
# initialise to all 0s
outPixels1 = [0] * (len(sourcePixels)*4)
outPixels2 = [0] * (len(sourcePixels)*4)

# for each pixel in the original, create a 2x2 pixel grid
for i in range(0, width):
  for j in range(0, height):
# ***********************************************************************
# IF USING THIS FOR A SERIOUS CRYPTOGRAPHIC PURPOSES, (AS OPPOSED TO A 
# DEMONSTRACTION) ENSURE THAT THE LINE BELOW PROVIDES A GOOD SOURCE OF
# ENTROPY. IF NOT REPLACE IT WITH SOME OTHER SOURCE OF RANDOMNESS.
    randIndex = random.randint(0, 1) 
# ***********************************************************************
    randInverse = (randIndex+1) % 2 # the inverse of the above
    if sourcePixels[((j*width)+i)] > 128:
      # source pixel is white, so the pixel pattern should match
      outPixels1[(j*width*4)+(i*2)+randIndex] = 255
      outPixels1[(j*width*4)+(i*2)+(width*2)+randInverse] = 255
      outPixels2[(j*width*4)+(i*2)+randIndex] = 255
      outPixels2[(j*width*4)+(i*2)+(width*2)+randInverse] = 255
    else:
      # source pixel is black, so the pixel pattern should be opposed
      outPixels1[(j*width*4)+(i*2)+randIndex] = 255
      outPixels1[(j*width*4)+(i*2)+(width*2)+randInverse] = 255
      outPixels2[(j*width*4)+(i*2)+randInverse] = 255
      outPixels2[(j*width*4)+(i*2)+(width*2)+randIndex] = 255

# create and save output files
outIm1 = Image.new('L', (width*2, height*2))
outIm1.putdata(outPixels1)
outIm2 = Image.new('L', (width*2, height*2))
outIm2.putdata(outPixels2)

rootF = sys.argv[1].rsplit(".",1)[0]
outIm1.save(rootF+"_1.png")
outIm2.save(rootF+"_2.png")
