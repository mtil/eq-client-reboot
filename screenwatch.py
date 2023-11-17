import cv2
import numpy as np
from PIL import ImageGrab

# Load the target image you want to search for
target_image = cv2.imread('error.png', cv2.IMREAD_UNCHANGED)

def watch_screen():
    while True:
        # Capture the screen
        screenshot = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))  # Adjust coordinates to your screen resolution

        # Perform template matching
        result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Define a threshold (adjust as needed)
        threshold = 0.8

        if max_val >= threshold:
            print(f"Target image found at position {max_loc}")
            break

# Perform further actions when the target image is found
# For example, you can click on it using libraries like pyautogui, or perform other tasks.
