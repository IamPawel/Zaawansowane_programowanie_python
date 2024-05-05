import cv2
import numpy as np

# Wczytaj wytrenowany model YOLO
net = cv2.dnn.readNetFromDarknet('model/yolov3.cfg','model/yolov3.weights')


# Wczytaj zdjęcie
img = cv2.imread("input.jpg")
height, width, _ = img.shape

# Konwersja obrazu na format, który akceptuje YOLO (blob)
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

# Ustawienie wejścia do sieci neuronowej
net.setInput(blob)

# Wykonaj detekcję
output_layers_names = net.getUnconnectedOutLayersNames()
layer_outputs = net.forward(output_layers_names)

# Inicjalizacja zmiennych
boxes = []
confidences = []
class_ids = []

# Przeglądaj wyniki detekcji i zapisz interesujące nas informacje
for output in layer_outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5 and class_id == 0:  # Jeśli wykryto człowieka (klasa 0)
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Wyświetlanie wyników
num_people = len(boxes)
print("Liczba ludzi na zdjęciu:", num_people)

# Wyświetlenie obrazu z zaznaczonymi ramkami wokół ludzi
for i in range(len(boxes)):
    x, y, w, h = boxes[i]
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
