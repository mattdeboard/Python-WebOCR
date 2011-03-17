# Helper script for cleaning up/automating some of the manual tasks 
# associated with training Google's Tesseract OCR software. This script 
# is not dependent on any particular Python wrapper for Tesseract.
#
# See http://code.google.com/p/tesseract-ocr/wiki/ReadMe#Linux for more
# information on this.
# 
# Author: Matt DeBoard (matt.deboard@gmail.com)
# Homepage: http://mattdeboard.net

import os
import subprocess
import sys

def main():
    if len(sys.argv) not in (1, 2, 3):
        print >> sys.stderr, "usage: ./pt_helper.py <action> <tessdata abs path>"
        print >> sys.stderr, "Actions are: repair, clean."
        print >> sys.stderr, "Path defaults to current directory."

    if len(sys.argv) >= 2:
        action = sys.argv[1]
    else:
        action = 'repair'

    if len(sys.argv) >= 3:
        path = sys.argv[2]
    else:
        path = os.getcwd()

    if action not in ('repair', 'train'):
        return "Choices for action are repair and train."

    if action == 'repair':
        repair(path)
    else:
        train(path)
        

def repair(boxfile_directory):
    ''' This function renames all the files in Google's boxtiff-2.0.1.*
    training packs for Tesseract. They're bundled with deprecated file
    names.'''
    tif_files = []
    for filename in os.listdir(boxfile_directory):
        root, extension = os.path.splitext(filename)
        if extension == '.box':
            # Obviously adjust this to your particular batch of tiff/box 
            #file pairs. Your .tif files may not end in ".g4", I just
            # hardcoded for sake of expediency.
            os.rename(filename, ''.join(root + '.g4.box'))
        
    return "All files renamed."

def train(boxfile_directory):
    '''This function automates "training" multiple font or language files
    that Tesseract uses to deduce text elements from image files.'''
    for filename in os.listdir(boxfile_directory):
        root, extension = os.path.splitext(filename)
        subprocess.call(["tesseract", filename, root,
                         "nobatch","box.train.stderr"])
        subprocess.call(["unicharset_extractor", ''.join(root+'.box')])
    
    return "All boxfiles processed. Please check stderr for error messages."
 
if __name__ == "__main__":
    main()