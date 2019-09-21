import numpy as np
from PIL import Image
import cv2


def show(image):
    while True:
        Imaga = np.array(Image.open(image, "r"))
        cv2.imshow("Test", cv2.cvtColor(Imaga, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    show(input(">"))
