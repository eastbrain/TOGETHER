import os
import sys
import cv2
import warnings
import argparse
import imutils
import csv
import numpy as np
import pandas as pd

import pytesseract
from pytesseract import pytesseract
import PIL
from PIL import Image

import ast
import json

class Main:




############################################################################################################################
    def __init__(self):
       pass
############################################################################################################################
    def main(self):

       main = Main()

       warnings.filterwarnings('ignore')

       parser = argparse.ArgumentParser(description='MICROBIOME ATP version (gtphrase@eonelab.co.kr)')
       parser.add_argument('image' ,type=str,help='image files')

       args     = parser.parse_args(sys.argv[1:])
       img_file = args.image

       main.detection(img_file)

if __name__ == '__main__':
   main = Main()
   main.main()
