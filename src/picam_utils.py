#/usr/bin/python3
from datetime import datetime
import picamera

import time

def capture_still(name = "", cameraobj = None):
	"""
	Capture a still image and save it as [name (argument 1)].png
	If no name is specified datetime.isoformat is used
	
	picamera.camera object can be passed as argument 2 but not required
	"""
	if not name: name = str(datetime.now().isoformat())
	try:
		cam = cameraobj
		if not isinstance(cam,picamera.PiCamera):
			cam = picamera.PiCamera()
		cam.capture(name + '.png')
		print( "Captured picture: {}!".format(name + '.png') )
	except Exception as e:
		print(e)

def capture_video(name = "", seconds = 10, cameraobj = None):
	"""
	Capture a video and save it as [name (argument 1)]...
	If no name is specified datetime.isoformat is used
	
	picamera.camera object can be passed as argument 2 but not required
	"""
	if not name: name = str(datetime.now().isoformat())
	try:
		cam = cameraobj
		if not isinstance(cam,picamera.PiCamera):
			cam = picamera.PiCamera()
		cam.start_recording(name + '.h264')
		print( "Started recording: {} for {} seconds!".format(name + '.h264', seconds) )
		time.sleep(seconds)
		cam.stop_recording()
		print( "Stopped recording!" )
	except Exception as e:
		print(e)

def preview_camera(seconds = 5, cameraobj = None):
	"""
	Show a preview of the camera for 5 seconds
	The amount of seconds can be passed as the first argument
	"""
	try:
		cam = cameraobj
		if not isinstance(cam,picamera.PiCamera):
				cam = picamera.PiCamera()
		cam.start_preview()
		time.sleep(seconds)
		cam.stop_preview()

	except Exception as e:
		print(e)
