"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2

from gaze_tracking import GazeTracking
import numpy as np

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
notComplete = True
calibration_const = 1000
screen_width = 4500
screen_height = 2500




def get_right():
    text = "Calibration Right: Look at the Dot and Click Enter"
    textDot = "."
    cv2.putText(new_frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(new_frame, textDot, (2250 + calibration_const, 1250), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    if cv2.waitKey(1) == 13:
        gaze.set_self_right()

def get_left():
    text = "Calibration Left: Look at the Dot and Click Enter"
    textDot = "."
    cv2.putText(new_frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(new_frame, textDot, (2250 - calibration_const, 1250), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    if cv2.waitKey(1) == 13:
        gaze.set_self_left()

def get_up():
    text = "Calibration Up: Look at the Dot and Click Enter"
    textDot = "."
    cv2.putText(new_frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(new_frame, textDot, (2250, 1250 - calibration_const), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    if cv2.waitKey(1) == 13:
        gaze.set_self_up()

def get_down():
    text = "Calibration Down: Look at the Dot and Click Enter"
    textDot = "."
    cv2.putText(new_frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(new_frame, textDot, (2250, 1250 + calibration_const), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    if cv2.waitKey(1) == 13:
        gaze.set_self_down()

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    new_frame = np.zeros((2500, 4500, 3), np.uint8)
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    textLR = ""
    textUD = ""

    if gaze.get_self_right() is None:
        get_right()
    elif gaze.get_self_left() is None:
        get_left()
    elif gaze.get_self_up() is None:
        get_up()
    elif gaze.get_self_down() is None:
        get_down()
    else:
        if gaze.is_up():
            textUD = "Looking up"
        elif gaze.is_down():
            textUD = "Looking down"
        else:
            textUD = "Centered"

        if gaze.is_left():
            textLR = "Looking left"
        elif gaze.is_right():
            textLR = "Looking right"
        else:
            textLR = "Centered"

    cv2.putText(frame, textUD, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(frame, textLR, (90, 160), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    cv2.imshow("Demo", frame)
    cv2.imshow("new", new_frame)

    if cv2.waitKey(1) == 27:
        break
  
webcam.release()
cv2.destroyAllWindows()
