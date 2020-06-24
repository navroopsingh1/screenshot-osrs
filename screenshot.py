import pyscreenshot as ImageGrab
from datetime import datetime

# part of the screen
im = ImageGrab.grab(bbox=(0, 25, 765, 480))  # X1,Y1,X2,Y2
dt = datetime.now()
# save image file
fname = "img/pic_{}.{}.png".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)
im.save(fname,'png')