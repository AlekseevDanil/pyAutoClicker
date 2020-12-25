# -*- coding: utf-8 -*-
# Загружаем нужные пакеты
import pyautogui
import keyboard

# бираем кнопки старта программы и остановки
key_start = input("Выберете кнопку старта кликера (eng): ")
key_stop = input("Выберете кнопку завершения кликера (eng): ")

# Запускаем программу
while True:
    if keyboard.is_pressed(key_start):
        pyautogui.doubleClick()

    if keyboard.is_pressed(key_stop):
        break
