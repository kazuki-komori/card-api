import cv2
from unittest import TestCase
from src.colorPicker import ColorPicker


class ColorPickerTest(TestCase):

    def test_main(self):
        img = cv2.imread('../data/test.jpg')
        self.assertEqual(bool(ColorPicker(img).main()), True)
