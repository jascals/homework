# coding:utf-8
# auther:cherie

from PIL import Image, ImageDraw, ImageFont
import glob, os


def mark(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:\WINDOWS\Fonts\Arial.ttf', size=26)
    fillcolor = "#000000"
    width, height = img.size
    draw.text((width - 100, 0), 'mashiro', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    return 0


if __name__ == '__main__':
    image = Image.open('pokemen.png')

    # The following script loads an image, rotates it 45 degrees, and displays it using an external viewer
    image.rotate(0).show()

    # The following script creates nice 128x128 thumbnails of all JPEG images in the current directory.
    '''
    size = 128, 128
    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")
    '''

    mark(image)
