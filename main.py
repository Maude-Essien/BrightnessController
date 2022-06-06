import cv2


def BrightnessControl(brightness=0):

    # getTrackbarPos returns the current position of the specified trackbar.
    brightness = cv2.getTrackbarPos('Brightness', 'Brightness Controller')

    # effect is variable that displays the results when the trackbar is moved.
    effect = controller(img, brightness)

    # The function imshow displays an image in the specified window
    cv2.imshow('Effect', effect)


def controller(image, brightness=255):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))

    # This If function checks for the brightness of the image and adjusts it in relation to a set maximum brightness.
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            maximum = 255
        else:
            shadow = 0
            maximum = 255 + brightness
        alpha = (maximum - shadow) / 255
        gamma = shadow

        # The function addWeighted calculates the weighted sum of two arrays
        cal = cv2.addWeighted(image, alpha, image, 0, gamma)
    else:
        cal = image
    return cal


if __name__ == '__main__':
    # The function imread loads an image from the specified file and returns it.
    original = cv2.imread("tryimg.jpg")

    # Making another copy of an image.
    img = original.copy()

    # The function namedWindow creates a window that can be used as a placeholder for images.
    cv2.namedWindow('Brightness Controller')

    # The function imshow displays an image in the specified window.
    cv2.imshow('Brightness Controller', original)

    # createTrackbar(trackbarName, windowName, value, count, onChange) Brightness range -255 to 255
    cv2.createTrackbar('Brightness', 'Brightness Controller', 255, 2 * 255, BrightnessControl)

    BrightnessControl(0)

# The function waitKey waits for a key event infinitely or for delay milliseconds, when it is positive.
cv2.waitKey(0)
