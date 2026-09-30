# Driver Drowsiness Detection using OpenCV
# Author: Bodimalla Mokshitha | ECE | GPCET Kurnool

import cv2
import dlib
from scipy.spatial import distance
import time

# Eye Aspect Ratio calculation
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Constants
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 48

# Initialize
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

print("Driver Drowsiness Detection System Started")
print("Tech Stack: Python, OpenCV, Dlib, Scipy")
