import keyboard
import mouse
import time

check=False
while(True):
    print(check)
    if(keyboard.is_pressed("F1")):
        check=True
    if(check==True):
        mouse.click(button='left')
        for i in range(30):
            if(keyboard.is_pressed("F2")):
                check=False
                break
            time.sleep(0.01)