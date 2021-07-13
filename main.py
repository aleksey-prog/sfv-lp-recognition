import cv2
import pyautogui
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ---------------------------------------------------------------------------------------------------------------------
# Finding left League Points
# ---------------------------------------------------------------------------------------------------------------------
league_points_left = pyautogui.screenshot(region=(350, 400, 200, 45))
opencv_league_points_left = cv2.cvtColor(np.array(league_points_left), cv2.COLOR_RGB2BGR)

gray_league_points_left = cv2.cvtColor(opencv_league_points_left, cv2.COLOR_BGR2GRAY)
threshold_league_points_left = cv2.threshold(gray_league_points_left, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

text1 = pytesseract.image_to_string(threshold_league_points_left)
print(text1)

# ---------------------------------------------------------------------------------------------------------------------
# Finding left Nickname
# ---------------------------------------------------------------------------------------------------------------------
nickname_left = pyautogui.screenshot(region=(222, 306, 200, 45))
opencv_nickname_left = cv2.cvtColor(np.array(nickname_left), cv2.COLOR_RGB2BGR)

gray_nickname_left = cv2.cvtColor(opencv_nickname_left, cv2.COLOR_BGR2GRAY)
threshold_nickname_left = cv2.threshold(gray_nickname_left, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

text2 = pytesseract.image_to_string(threshold_nickname_left)
print(text2)

# ---------------------------------------------------------------------------------------------------------------------
# Finding right League Points
# ---------------------------------------------------------------------------------------------------------------------
league_points_right = pyautogui.screenshot(region=(1680, 418, 135, 45))
opencv_league_points_right = cv2.cvtColor(np.array(league_points_right), cv2.COLOR_RGB2BGR)

gray_league_points_right = cv2.cvtColor(opencv_league_points_right, cv2.COLOR_BGR2GRAY)
threshold_league_points_right = cv2.threshold(gray_league_points_right, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

text3 = pytesseract.image_to_string(threshold_league_points_right)
print(text3)

# ---------------------------------------------------------------------------------------------------------------------
# Finding right Nickname
# ---------------------------------------------------------------------------------------------------------------------
nickname_right = pyautogui.screenshot(region=(1470, 307, 250, 45))
opencv_nickname_right = cv2.cvtColor(np.array(nickname_right), cv2.COLOR_RGB2BGR)

gray_nickname_right = cv2.cvtColor(opencv_nickname_right, cv2.COLOR_BGR2GRAY)
threshold_nickname_right = cv2.threshold(gray_nickname_right, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

text4 = pytesseract.image_to_string(threshold_nickname_right)
print(text4)

cv2.imshow('threshold image', threshold_nickname_right)
cv2.waitKey(0)
cv2.destroyAllWindows()
