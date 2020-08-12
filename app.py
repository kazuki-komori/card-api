from src.colorPicker import ColorPicker
import cv2


def getColor():
    img = cv2.imread('./data/green.jpg')
    print(ColorPicker(img).main())


getColor()
