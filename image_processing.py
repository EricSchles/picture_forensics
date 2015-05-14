import Image
import exifread
from LSBSteg import LSBSteg
import cv

def hide_data(in_img,data):
    carrier = cv.LoadImage(in_img)
    steg = LSBSteg(carrier)
    steg.hideText(data)
    out_img = in_img.split(".")[0]+".png"
    steg.saveImage(out_img)
    return out_img

def retrieve_data(img):
    print img
    im = cv.LoadImage(img)
    steg = LSBSteg(im)
    return steg.unhideText()

def exif_preserve(img_name,new_path=''):
    img = Image.open(img_name)
    try:
        exif = img.info['exif']
    except KeyError:
        return "no exif"
    if new_path == '':
        img.save(img_name.filename,exif=exif)
    else:
        img.save(new_path,exif=exif)
    return "success"

def exif_strip(img_path,new_path=''):
    img = Image.open(img_path)
    if new_path == '':
        new_img_path = "stripped"+img_path
    else:
        new_img_path = new_path
    img.save(new_img_path)
    return new_img_path

def exif_enumerate(img_path):
    f = open(img_path,"rb")
    tags = exifread.process_file(f)
    return str(tags)

