import cv2
import pygame
import time

# Инициализация библиотеки pygame для воспроизведения звука
pygame.mixer.init()

# Функция для воспроизведения звука
def play_sound():
    pygame.mixer.music.load("/home/lina1/Desktop/project/claymore_ringtone.mp3")  # путь к звуковому файлу
    pygame.mixer.music.play()

# Загрузка классификатора для обнаружения объектов (котов)
cat_cascade = cv2.CascadeClassifier("/home/lina1/Desktop/project/haarcascade_frontalcatface.xml")
if cat_cascade.empty():
	print("ошибка загрузки каскада. проверьте путь и файл")
