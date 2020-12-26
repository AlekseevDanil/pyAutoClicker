# -*- coding: utf-8 -*-
# Download the required packages
import pyautogui
import keyboard


# This function starts auto clicker only when you press a button
def holdButton(key_start="s", key_stop="t"):
    while True:
        # Works as long as the button is pressed, and stops as soon as we release the button
        if keyboard.is_pressed(key_start):
            pyautogui.tripleClick()
        # When pressed, ends the program
        if keyboard.is_pressed(key_stop):
            break


# This function starts auto clicker only when you hold down the button
def pushButton(key_start="s", key_pause="p", key_stop="t"):
    p = 1
    while True:
        while p == 1:
            # Runs the program after clicking on the button
            if keyboard.is_pressed(key_start):
                p = 0
        # Pauses auto click
        if keyboard.is_pressed(key_pause):
            p = 1
            continue
        # When pressed, ends the program
        if keyboard.is_pressed(key_stop):
            break
        pyautogui.tripleClick()


if __name__ == "__main__":
    # [INFO] An example of a possible program:
    print("\n - Hello in test mode pyAutoClicker! - \n")
    mode = input("Choose a mode and write only its number!\n1 - Hold the button\n2 - Press the button\n>>> ")
    while mode.strip() != "1" and mode.strip() != "2":
        mode = input("Let's try again :)\nWrite only the mode number!")
    key_start = input("Select the button to enable the clicker (eng)\n>>> ")
    if mode.strip() == "2":
        key_pause = input("Select the pause clicker button (eng)\n>>> ")
    key_stop = input("Select the end clicker button (eng)\n>>> ")

    print("Fine! The program is running and ready to work")
    if mode.strip() == "1":
        print("Just move the mouse over the place you need and hold down the button to enable the clicker")
    elif mode.strip() == "2":
        print("Just move the mouse over the place you need and click on the button to enable the clicker")
    print("[INFO] To turn off the program, press the off button")

    # Using the functions described earlier
    if mode.strip() == "1":
        holdButton(key_start=key_start,
                   key_stop=key_stop)
    elif mode.strip() == "2":
        pushButton(key_start=key_start,
                   key_pause=key_pause,
                   key_stop=key_stop)

    print("\nTest over, have a nice day! :-)")
