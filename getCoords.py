import pyautogui as auto
import sys
import random
import time

def getCoords():
    try:
        while True:
            x, y = auto.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr),
            print('\b' * (len(positionStr) + 2)),
            sys.stdout.flush()
    except KeyboardInterrupt:
        print('\n')

def main():
    getCoords()
    

if __name__ == "__main__":
  main()
