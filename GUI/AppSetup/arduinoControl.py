from Arduino import *
import time


class arduinoControl:

    def __init__(self):
        self.board = Arduino("115200", port="/dev/tty.usbmodem142301")

        self.board.pinMode(13, "OUTPUT")
