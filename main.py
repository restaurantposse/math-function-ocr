import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def read_function(path):
    img = cv2.imread(path)
    ocr_output = pytesseract.image_to_string(img).replace(' ', '')
    return ocr_output


def do_math(ocr_output):
    if '=' not in ocr_output:
        raise f'Invalid OCR output. {ocr_output}'
    left, right = ocr_output.split('=')
    x = np.linspace(-10,10,100)
    if right[0] == '-':
        if right[1].isdigit():
            right = right.replace('x', '*x')
    elif right[0].isdigit():
        right = right.replace('x', '*x')
    y = eval(right)
    plt.plot(x, y)  # plot the x and y values
    plt.xlabel('x')  # label the x-axis
    plt.ylabel('y')  # label the y-axis
    plt.title(f'{ocr_output}')  # title the plot
    plt.show()  # show the plot


ocr_result = read_function('img/img_1.png')
do_math(ocr_result)
