import cv2
import numpy as np
from math import sqrt, acos

def gest_recognition():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.rectangle(frame, (300, 300), (100, 100), (0, 255, 0), 0)
        frame_roi = frame[100:300, 100:300]
        gray = cv2.cvtColor(frame_roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (35, 35), 0)
        _, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        cv2.imshow('Threshold_frame', thresh)
        (version, _, _) = cv2.__version__.split('.')

        if version == '3':
            img, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        elif version == '2':
            contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        maxarea_contour = max(contours, key=lambda x: cv2.contourArea(x))
        x, y, w, h = cv2.boundingRect(maxarea_contour)
        cv2.rectangle(frame_roi, (x, y), (x+w, y+h), (0, 0, 255), 0)

        hull = cv2.convexHull(maxarea_contour)
        drawing = np.zeros(frame_roi.shape, np.uint8)
        cv2.drawContours(drawing, [maxarea_contour], 0, (0, 255, 0), 0)
        cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 0)

        hull = cv2.convexHull(maxarea_contour, returnPoints=False)
        defects = cv2.convexityDefects(maxarea_contour, hull)
        defects_count = 0
        cv2.drawContours(thresh, contours, -1, (0, 255, 0), 3)

        for defect in range(defects.shape[0]):
            s, e, f, d = defects[defect, 0]

            start = tuple(maxarea_contour[s][0])
            end = tuple(maxarea_contour[e][0])
            far = tuple(maxarea_contour[f][0])
            a = sqrt((end[0]-start[0]) **2 + (end[1]-start[1]) **2)
            b = sqrt((far[0]-start[0]) **2 + (far[1]-start[1]) **2)
            c = sqrt((end[0]-far[0]) **2 + (end[1]- far[1]) **2)

            angle = acos((b**2 + c**2 - a**2) / (2*b*c)) * 57

            if angle <= 90:
                defects_count += 1
                cv2.circle(frame_roi, far, 1, [0, 0, 255], -1)
            cv2.line(frame_roi, start, end, [0, 255, 0], 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        
        cv2.putText(frame, 'Please sign in the box! ', (50, 50), font, 1.5, (200, 255, 155), 5, cv2.LINE_AA)
        if defects_count == 1:
            cv2.putText(frame, "Gesture: Two!", (10, 450), font, 2, (200, 255, 155), 5, cv2.LINE_AA)
        elif defects_count == 2:           
            cv2.putText(frame, "Gesture: Three!", (10, 450), font, 2, (200, 255, 155), 5, cv2.LINE_AA)
        elif defects_count == 3:
            cv2.putText(frame,"Gesture: Four!", (10, 450), font, 2, (200, 255, 155), 5, cv2.LINE_AA)
        elif defects_count == 4:
            cv2.putText(frame, "Gesture: Five!", (10, 450), font, 2, (200, 255, 155), 5, cv2.LINE_AA)
        else:
            cv2.putText(frame, "Start from Two!", (50, 450), font, 1.5, (200, 255, 155), 5, cv2.LINE_AA)

        cv2.imshow('Gesture_frame', frame)
        frame_contour = np.hstack((drawing, frame_roi))
        cv2.imshow('Contours_frame', frame_contour)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
    cap.release()

#gest_recognition()
