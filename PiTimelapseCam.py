from time import sleep
from picamera import PiCamera

import datetime from datetime
import yaml
import os
import sys

def create_photo_dir(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != errno.EXIST:
            raise


newdir = os.path.join(
    sys.path[0],
    'series-' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

create_photo_dir(newdir)

camera = PiCamera()
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(60) # wait 1 minutes

