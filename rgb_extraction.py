# Python script to display all pixels RGB values
# from an image and output them a row at a time
#
# Import the PIL library - pip3 install Pillow
from PIL import Image
import glob
import matplotlib.pyplot as plt
images=glob.glob("A:\MINOR PROJECT\Heart-Rate-Detection-rPPg\dataset\*.png")

red = []
green = []
blue = []
count = 1;
for image in images:
    # Open our image
    im = Image.open(image)
    #print("Image : " + str(count))
    #count += 1
    # Convert our image to RGB
    rgb_im = im.convert('RGB')
     
    # Use the .size object to retrieve a tuple contain (width,height) of the image
    # and assign them to width and height variables
    width = rgb_im.size[0]
    height = rgb_im.size[1]
     
    # set some counters for current row and column and total pixels
    row = 1
    col = 1
    pix = 0
     
    # create an empty output row
    rowdata = ""
     
    # loop through each pixel in each row outputting RGB value as we go...
    # all the plus and minus ones are to deal with the .getpixel class being
    # zero indexed and we want the output to start at pixel 1,1 not 0,0!
    Red_val = 0
    Green_val = 0
    Blue_val = 0
    while row < height + 1:
        while col < width + 1:
            # get the RGB values from the current pixel
            r, g, b = rgb_im.getpixel((col - 1, row - 1))
            # Add all red , green and blue values
            Red_val += r
            Green_val += g
            Blue_val += b
            
            # increment the column count
            col = col + 1
            # increment the pixel count
            pix = pix + 1

        # increment the row...
        row = row + 1
        # reset the column count
        col = 1
 
    avg_red = Red_val / pix
    avg_green = Green_val / pix
    avg_blue = Blue_val / pix
   
    print(str(count) + ": "+ '('+ str(avg_red) + ',' + str(avg_green) + ',' + str(avg_blue) + ')')
    count += 1
    red.append(avg_red)
    green.append(avg_green)
    blue.append(avg_blue)

fig = plt.figure()

ax1 = fig.add_subplot(311)
ax1.plot(red, 'r')

ax2 = fig.add_subplot(312)
ax2.plot(blue , 'b')

ax3 = fig.add_subplot(313)
ax3.plot(green, 'g')

plt.show()
  
