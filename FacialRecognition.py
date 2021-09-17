# This code was created based on one seen on GeeksForGeeks.
# It is based on Computer Vision, and it includes the Open Source CV2
# package. What the code does is recognizing a face with with eyes
# and placing rectangles in front of the eyes and in the face as a whole.

# Alexa Serrano Negrete
# A01654063

import cv2

# The two xml docs to read facial expressions and eyes.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Captures frame by frame from a camera.
capture = cv2.VideoCapture(0)

# Loop runs if capturing has been initialized. 
while(True):
	# Reads frames from a camera
	ret, img = capture.read()

	# Converts to grayscale each frame
	grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Detects faces of different sizes in the input image
	faces = face_cascade.detectMultiScale(grayscale, 1.3, 5)

	# First for cycle:
	for(x, y, w, h) in faces:
		# Draws a rectangle in a face
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
		roi_gray = grayscale[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

		# Detects eyes of different sizes in the input image
		eyes = eye_cascade.detectMultiScale(roi_gray)

		# Draws rectangles in eyes
		for(ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh),
			(0, 127, 255), 2)

	# Displays an image in a window
	cv2.imshow('img',img)

	# Waits for Esc key to stop
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

capture.release()
cv2.destroyAllWindows()