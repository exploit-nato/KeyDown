import keyboard, time

while True:
    if(keyboard.is_pressed('esc')):
        keyboard.release('w')
        user = input("\rPaused: Press <Enter> To Continue, or Type 'Q' To Quit.\n->")
        if user.lower() == "q":
            break
    keyboard.press('w')
    time.sleep(0.1)