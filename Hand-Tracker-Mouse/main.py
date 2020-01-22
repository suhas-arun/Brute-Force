"""Hand tracker that controls the cursor"""
import cv2
import pyautogui

fist_cascade = cv2.CascadeClassifier("fist.xml")
palm_cascade = cv2.CascadeClassifier("palm.xml")

camera = cv2.VideoCapture(0)
window_width, window_height = camera.get(3), camera.get(4)
screen_width, screen_height = pyautogui.size()

while True:
    _, img = camera.read()

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    fists = fist_cascade.detectMultiScale(grey, 1.3, 5)
    palms = palm_cascade.detectMultiScale(grey, 1.3, 5)

    for fist in fists:
        x, y, width, height = fist
        cv2.rectangle(grey, (x, y), (x + width, y + height), (255, 255, 255), 2)

        width_ratio = screen_width / (window_width)
        height_ratio = screen_height / window_height

        if x < window_width / 2:
            x_pos = window_width - x

        else:
            x_pos = window_width - x - width

        if y > window_height / 2:
            y_pos = y + height
        else:
            y_pos = y

        mouse_x, mouse_y = x_pos * width_ratio, y_pos * height_ratio
        pyautogui.moveTo(x=mouse_x, y=mouse_y)

    for palm in palms:
        x, y, width, height = palm
        cv2.rectangle(grey, (x, y), (x + width, y + height), (0, 0, 0), 2)
        pyautogui.click()

    cv2.imshow("Image", cv2.flip(grey, 1))

    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()
