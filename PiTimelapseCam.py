from time import sleep
from picamera import PiCamera
from  datetime import datetime

import errno
import yaml
import os
import sys

cam_config = yaml.safe_load(open(os.path.join(sys.path[0], "Cam_config.yml")))

newdir = os.path.join(
            sys.path[0],
            'timelapse-' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

def create_photo_dir(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return

def capture_image():
    delay = 30
    quantity = 120
    camera = PiCamera()
    set_camera_options(camera)
    set_capture_options(delay, quantity)
    camera.start_preview()
    sleep(2)

    for filename in camera.capture_continuous(newdir + '/img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        print('Waiting %s' % delay)
        sleep(delay) # waits 30 seconds by default
    return

def set_camera_options(camera):
    if cam_config['resolution']:
            camera.resolution = (
                cam_config['resolution']['width'],
                cam_config['resolution']['height']
            )
    return(camera)

def set_capture_options(delay, quantity):
    if cam_config['capture_delay']:
            delay = cam_config['capture_delay']
    if cam_config['image_quantity']:
            quantity = cam_config['image_quantity']
    return(delay,quantity)

create_photo_dir(newdir)
capture_image()
