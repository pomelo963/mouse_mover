import pyautogui
import random
import time

def main():
    screen_width, screen_height = pyautogui.size()
    try:
        while True:
            
            x = random.randint(0, screen_width-1)
            y = random.randint(0, screen_height-1)
            pyautogui.moveTo(x, y, duration=0.5)
        
            time.sleep(random.randint(1, 5))
    except KeyboardInterrupt:
        print("Stopped by user")


if __name__ == "__main__":
    main()
