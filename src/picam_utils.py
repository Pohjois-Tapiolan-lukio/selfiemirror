#/usr/bin/python3
from datetime import datetime
import picamera

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
	except Exception as e:
		print(e)

def capture_video(name = "", cameraobj = None):
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
		cam.capture(name + '...')
	except Exception as e:
		print(e)
