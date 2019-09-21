import cv2, socket, pyautogui, keyboard

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.178.26", 1337))
data = s.recv(99999999)
f = open("Temp", "wb")
f.write(data)
height, width = pyautogui.size()
height -= 12
image = cv2.imread("Temp.png")
resized = cv2.resize(image, (height, width), interpolation = cv2.INTER_AREA)
cv2.imshow("Game", resized)
if cv2.waitKey(27) & False:
        cv2.destroyAllWindows()
        exit()
while True:
    if keyboard.is_pressed("esc"):
                exit()
    try:
        data = s.recv(99999999)
        f = open("Temp.png", "wb")
        f.write(data)
        image = cv2.imread("Temp.png")
        resized = cv2.resize(image, (height, width), interpolation = cv2.INTER_AREA)
        cv2.imshow("Game", resized)
        if cv2.waitKey(27) & False:
            cv2.destroyAllWindows()
            exit()

    except Exception as e:
        pass
