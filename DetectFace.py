import numpy as np
import cv2


def face_detection():
	face_cascade = cv2.CascadeClassifier('./assets/haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('./assets/haarcascade_eye.xml')

	cap = cv2.VideoCapture(0)
	prev_facelen = 0

	while True:
		ret, frame = cap.read()
		frame = cv2.flip(frame, 1)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray)
		curr_facelen = len(faces)

		for (fx, fy, fw, fh) in faces:
			cv2.rectangle(frame, (fx, fy), (fx+fw, fy+fh), (255, 0, 0), 2)
			roi_gray = gray[fy:fy+fh, fx:fx+fw]
			roi_color = frame[fy:fy+fh, fx:fx+fw]

			eyes = eye_cascade.detectMultiScale(roi_gray)
			for (ex, ey, ew, eh) in eyes:
				cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

		font = cv2.FONT_HERSHEY_SIMPLEX

		cv2.putText(frame, 'Faces: ', (10, 450), font, 2, (200, 255, 155), 5, cv2.LINE_AA)
		cv2.putText(frame, str(len(faces)), (210, 450), font, 2, (200, 255, 155), 5, cv2.LINE_AA)

		cv2.imshow('Face_frame', frame)
		if prev_facelen != curr_facelen:
			print ("No. of faces: ", len(faces))
		prev_facelen = curr_facelen

		if cv2.waitKey(5) & 0xFF == 27:
			break

	cv2.destroyAllWindows()
	cap.release()

#face_detection()
