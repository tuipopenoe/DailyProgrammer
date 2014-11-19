#!python2
# Tui Popenoe
# challenge179e.py - Convert Image to Grayscale

from PIL import Image

def grayscale(imagefile='image.jpg'):
    """Convert the image file to grayscale."""
    im = Image.open(imagefile)
    pix = im.load()
    print('Image Size: ' + str(im.size))
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            gray = sum(pix[i, j]) /3
            pix[i, j] = (gray, gray, gray)
    grayscale = im.save(imagefile, 'JPEG')

def main():
    grayscale()

if __name__ == '__main__':
    main()