from LSBSteg import LSBSteg
import cv
from sys import argv
#Hide
string = "Hello there"
carrier = cv.LoadImage(argv[1])
steg = LSBSteg(carrier)
steg.hideText(string)
steg.saveImage("hidden.png")

#retrieve
im = cv.LoadImage("hidden.png")
steg2 = LSBSteg(im)
print steg2.unhideText()
