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
	
# Открытие камеры
cap = cv2.VideoCapture(0)

while True:
    # Считывание кадра с камеры
    ret, frame = cap.read()

    if not ret:
        break

    # Преобразование изображения в оттенки серого для обработки
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Обнаружение кота на изображении
    cats = cat_cascade.detectMultiScale(gray, 1.1, 4)
