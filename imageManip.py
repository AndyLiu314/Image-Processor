# Filename: imageManip.py
# Author(s): Andy Liu and Harjap Gosal
# Date: Nov 30, 2021
# Date Last Edited: Dec 5, 2021
# Description: Final Project

import imageProjHelper as ph
import copy


# Manipulation Functions

# Function to apply red filter to image
# Retains the R value of all pixels in the image, and sets G and B to zero.
def applyRedFilter(pixels):
    manip_image = ph.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        manip_image[row][col][0] = pixels[row][col][0]
        manip_image[row][col][1] = 0
        manip_image[row][col][2] = 0
    
    return manip_image


# Function to apply green filter to image
# Retains the G value of all pixels in the image, and sets R and B to zero.
def applyGreenFilter(pixels):
    manip_image = ph.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        manip_image[row][col][0] = 0
        manip_image[row][col][1] = pixels[row][col][1]
        manip_image[row][col][2] = 0
       
    return manip_image


# Function to apply blue filter to image
# Retains the B value of all pixels in the image, and sets R and G to zero.
def applyBlueFilter(pixels):
    manip_image = ph.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        manip_image[row][col][0] = 0
        manip_image[row][col][1] = 0
        manip_image[row][col][2] = pixels[row][col][2]
    
    return manip_image


# Function to apply sepia filter to image
# Gives all colours with warm brownish tone
def applySepiaFilter(pixels):
    manip_image = ph.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        sepia_r = pixels[row][col][0]
        sepia_g = pixels[row][col][1]
        sepia_b = pixels[row][col][2]

        if int((sepia_r * 0.393) + (sepia_g * 0.769) + (sepia_b * 0.189)) < 255:
          manip_image[row][col][0] = int((sepia_r * 0.393) + (sepia_g * 0.769) + (sepia_b * 0.189))
        else: 
          manip_image[row][col][0] = 255

        if int((sepia_r * 0.349) + (sepia_g * 0.686) + (sepia_b * 0.168)) < 255:
          manip_image[row][col][1] = int((sepia_r * 0.349) + (sepia_g * 0.686) + (sepia_b * 0.168))
        else: 
          manip_image[row][col][1] = 255

        if int((sepia_r * 0.272) + (sepia_g * 0.534) + (sepia_b * 0.131)) < 255:
          manip_image[row][col][2] = int((sepia_r * 0.272) + (sepia_g * 0.534) + (sepia_b * 0.131))
        else:
          manip_image[row][col][2] = 255

    return manip_image


# Function to scale up depending on the value of the colours
def scaleUp(value):
  if value < 64:
    return int((value/64) * 80)
  elif 128 > value >= 64:
    return int(((value - 64)/(128 - 64)) * (160 - 80)) + 80
  else:
    return int(((value - 128)/(255 - 128)) * (255 - 160)) + 160


# Function to scale down depending on the value of the colours
def scaleDown(value):
  if value < 64:
    return int((value/64) * 50) 
  elif 128 > value >= 64:
    return int(((value - 64)/(128 - 64)) * (100 - 50)) + 50
  else:
    return int(((value - 128)/(255 - 128)) * (255 - 100)) + 100


# Function to apply warm filter to image
# Gives all colours a warm tone (calculated by scaling R values up and B values down)
def applyWarmFilter(pixels):
    manip_image = ph.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        manip_image[row][col][0] = scaleUp(pixels[row][col][0])
        manip_image[row][col][1] = pixels[row][col][1]
        manip_image[row][col][2] = scaleDown(pixels[row][col][2])

    return manip_image


# Function to apply cold filter to image
# Gives all colours a cold tone (calculated by scaling R down and B values up)
def applyColdFilter(pixels):
    manip_image = ph.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        manip_image[row][col][0] = scaleDown(pixels[row][col][0])
        manip_image[row][col][1] = pixels[row][col][1]
        manip_image[row][col][2] = scaleUp(pixels[row][col][2])

    return manip_image


# Advanced functions start here

# Function to rotate left the image
# Rotates the image counter-clockwise by 90 degrees
# Sets the original width equal to length and the original length equal to width
def rotateLeft(pixels):
    length = len(pixels)
    width = len(pixels[0])
    manip_image = ph.getBlackImage(length, width)
    for row in range(length):
      for col in range(width):
        manip_image[width - col - 1][row] = pixels[row][col]

    return manip_image


# Function to rotate right the image
# Rotates the image clockwise by 90 degrees
def rotateRight(pixels):
    length = len(pixels)
    width = len(pixels[0])
    manip_image = ph.getBlackImage(length, width)
    for row in range(length):
      for col in range(width):
        manip_image[col][length - row - 1] = pixels[row][col]

    return manip_image


# Function to half size image
# Halves both width and height (image size is reduced by 1/4)
def halfSize(pixels):
    length = len(pixels)
    width = len(pixels[0])
    manip_image = ph.getBlackImage(int(width/2), int(length/2))
    # r, g, b implies red, green, blue in the following code
    # averages the rgb values of 4 pixels of the original image into 1 pixel
    for row in range(length - 1):
      for col in range(width - 1):
        r_pixel1 = pixels[row][col][0]
        r_pixel2 = pixels[row + 1][col][0]
        r_pixel3 = pixels[row][col + 1][0]
        r_pixel4 = pixels[row + 1][col + 1][0]
        red_avg = int((r_pixel1 + r_pixel2 + r_pixel3 + r_pixel4)/4)

        g_pixel1 = pixels[row][col][1]
        g_pixel2 = pixels[row + 1][col][1]
        g_pixel3 = pixels[row][col + 1][1]
        g_pixel4 = pixels[row + 1][col + 1][1]
        green_avg = int((g_pixel1 + g_pixel2 + g_pixel3 + g_pixel4)/4)

        b_pixel1 = pixels[row][col][2]
        b_pixel2 = pixels[row + 1][col][2]
        b_pixel3 = pixels[row][col + 1][2]
        b_pixel4 = pixels[row + 1][col + 1][2]
        blue_avg = int((b_pixel1 + b_pixel2 + b_pixel3 + b_pixel4)/4)

        manip_image[int(row/2)][int(col/2)] = [red_avg, green_avg, blue_avg]

    return manip_image


# Function to double size image 
# Doubles both the width and height (image size increases 4 times)
# Every original pixel becomes a 2x2 block of pixels
def doubleSize(pixels):
    length = len(pixels)
    width = len(pixels[0])
    manip_image = ph.getBlackImage(2 * width, 2 * length)
    for row in range(length):
      for col in range(width):
        manip_image[2 * row][2 * col] = pixels[row][col]
        manip_image[2 * row + 1][2 * col] = pixels[row][col]
        manip_image[2 * row][2 * col + 1] = pixels[row][col]
        manip_image[2 * row + 1][2 * col + 1] = pixels[row][col]

    return manip_image


# Function to locate fish in image
# Locates fish by first detecting the yellow colour with ph.rbg_to_hsv
# Then draws a green box around the fish
def locateFish(pixels):
  length = len(pixels)
  width = len(pixels[0])
  manip_image = copy.deepcopy(pixels)
  left_border = 0
  right_border = 0
  top_border = 0
  bottom_border = 0
  locate_fish = False

  for row in range(length):
    for col in range(width):
      hsv = ph.rgb_to_hsv(pixels[row][col][0], pixels[row][col][1], pixels[row][col][2])
      hue = hsv[0]
      sat = hsv[1]
      value = hsv[2]

      if 75 >= hue >= 55 and 100 >= sat >= 45 and 100 >= value >= 80:
        if locate_fish == False:
          left_border = col
          right_border = col
          top_border = row
        bottom_border = row

        if col > right_border:
          right_border = col

        if col < left_border:
          left_border = col

        locate_fish = True

  if locate_fish == True:
    for row in range(length):
      for col in range(width):
        if col == right_border and bottom_border >= row >= top_border:
          manip_image[row][col] = [0,255,0]

        if col == left_border and bottom_border >= row >= top_border:
          manip_image[row][col] = [0,255,0]

        if row == top_border and right_border >= col >= left_border:
          manip_image[row][col] = [0,255,0]

        if row == bottom_border and right_border >= col >= left_border:
          manip_image[row][col] = [0,255,0]

  return manip_image
