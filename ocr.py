try:
    import Image
except ImportError:
    from PIL import Image, ImageGrab
import pytesseract
from pytesseract import Output
from os import getcwd
from time import sleep
import cv2

class OCR:
    
    def __init__(self):
        
        pass
        
                
    def get_text(self, filename):
        
        img = cv2.imread('img.png')

        # Path to Tesseract Executable
        pytesseract.pytesseract.tesseract_cmd = getcwd() + r'\Tesseract-OCR\tesseract.exe'

        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        textboxes = []

        for i in range(len(d['level'])):
            box = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            text = d['text'][i]
            if text != '':
                textboxes.append((box, text))

        return textboxes