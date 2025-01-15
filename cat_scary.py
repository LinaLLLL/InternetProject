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
    
    if len(cats) > 0:
    
        # Если кот найден, записываем в файл (моделируем работу с портами)
        with open("/home/lina1/Desktop/project/cat_detected", "w") as f:
            f.write("Cat detected!")

        # Воспроизведение звука
        play_sound()
        time.sleep(3)  # Задержка для предотвращения многократного воспроизведения звука
        
        # Сохранение скриншота
        screenshot_path = f"/home/lina1/Desktop/project/screenshot_{int(time.time())}.png"
        cv2.imwrite(screenshot_path, frame)
        
    # Отображение видео
    for (x, y, w, h) in cats:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
    cv2.imshow("Cat Detector", frame)
        
    # Прерывание цикла при нажатии клавиши ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
