# -*- coding: utf-8 -*-
# Download the required packages
import pyautogui
import keyboard


def holdButton(key_start="s", key_stop="t"):
    while True:
        if keyboard.is_pressed(key_start):
            pyautogui.tripleClick()
        if keyboard.is_pressed(key_stop):
            break


def pushButton(key_start="s", key_pause="p", key_stop="t"):
    p = 1
    while True:
        while p == 1:
            if keyboard.is_pressed(key_start):
                p = 0
        if keyboard.is_pressed(key_pause):
            p = 1
            continue
        if keyboard.is_pressed(key_stop):
            break
        pyautogui.tripleClick()


if __name__ == "__main__":
    print("\nПриветствую!\n")
    mode = input("Выберете режим и напишите только его цифру!\n1 - Зажать кнопку\n2 - Нажать кнопку\n>>> ")
    while mode.strip() != "1" and mode.strip() != "2":
        mode = input("Давайте попробуем еще раз :)\nНапишите только цифру режима!")
    key_start = input("Выберете кнопку включения кликера (eng)\n>>> ")
    if mode.strip() == "2":
        key_pause = input("Выберете кнопку паузы кликера (eng)\n>>> ")
    key_stop = input("Выберете кнопку завершения кликера (eng)\n>>> ")

    print("Отлично! Программа запущенна и готова к работе")
    if mode.strip() == "1":
        print("Просто наведите мышку на нужное вам место и зажмите кноку включения кликера")
    elif mode.strip() == "2":
        print("Просто наведите мышку на нужное вам место и нажмите на кноку включения кликера")
    print("[INFO] Для выключения программы нажмите кнопку выключения")

    if mode.strip() == "1":
        holdButton(key_start=key_start,
                   key_stop=key_stop)
    elif mode.strip() == "2":
        pushButton(key_start=key_start,
                   key_pause=key_pause,
                   key_stop=key_stop)

    print("\nEnded!")
