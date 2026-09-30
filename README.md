# Driver Drowsiness Detection 😴🚗 - AI Safety Project

## Overview
Real-time driver drowsiness detection system using Computer Vision to prevent road accidents by monitoring eye closure and alerting driver.

## Features
- Real-time Eye Blink Monitoring
- Eye Aspect Ratio (EAR) Calculation
- Drowsiness Alert System with Alarm
- Face Landmark Detection (68 points)
- Works in Low Light Conditions

## Tech Stack
- **Language:** Python 3.8+
- **Libraries:** OpenCV, Dlib, Scipy, Numpy, Pygame
- **Model:** 68 Face Landmarks Predictor
- **Concepts:** Computer Vision, EAR Algorithm

## How it Works
1. Detects face using HOG
2. Extracts eye landmarks
3. Calculates EAR value
4. If EAR < 0.25 for 48 frames -> Drowsy -> Alarm

## Future Scope
- Integration with IoT (Smart Helmet)
- GSM Alert to family
- Cloud Dashboard

## Author
Bodimalla Mokshitha | B.Tech ECE 3rd Year | GPCET Kurnool | CGPA 8.5
GitHub: BodimallaMokshitha

## Application
Automotive Safety, Fleet Management, Driver Monitoring Systems
