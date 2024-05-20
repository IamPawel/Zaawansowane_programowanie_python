import uuid
import time
import json
import os
import cv2 as cv
import base64
import imghdr
import numpy as np
import requests

cvNet = cv.dnn.readNetFromTensorflow(
    "models/frozen_inference_graph.pb", "models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt"
)
img_link = "https://konteksthr.pl/wp-content/uploads/2015/02/ludzie_2.jpg"
img_path = "input.jpg"


def img_to_base64(img):
    _, img_encoded = cv.imencode(".jpg", img)
    img_base64 = base64.b64encode(img_encoded)
    return img_base64.decode("utf-8")


img_base = img_to_base64(cv.imread(img_path))
print(img_base[:10])


def download_image(url):
    response = requests.get(url)
    image_array = np.asarray(bytearray(response.content), dtype="uint8")
    img = cv.imdecode(image_array, cv.IMREAD_COLOR)
    return img


def generate_json(img, type):
    data = {
        "uuid": str(uuid.uuid4()),
        "timestamp": int(time.time()),
        "file": img,
        "type": type,
    }
    return json.dumps(data)


body = f"{generate_json(img_base, 'file')}"
# print(body)

# print(json.loads(body))


def read_json(data):
    data = json.loads(data)
    file_data = data["file"]
    file_type = data["type"]
    file_id = data["uuid"]
    file_timestamp = data["timestamp"]

    if file_type == "file":
        image_data = base64.b64decode(file_data)
        image_extension = imghdr.what(None, h=image_data)
        image_array = np.frombuffer(image_data, dtype=np.uint8)
        img = cv.imdecode(image_array, cv.IMREAD_COLOR)
        return img, file_id, file_timestamp, image_extension

    elif file_type == "path":
        _, image_extension = os.path.splitext(file_data)
        img = cv.imread(file_data)
        return img, file_id, file_timestamp, image_extension

    elif file_type == "link":
        _, image_extension = os.path.splitext(file_data)
        response = requests.get(file_data)
        image_array = np.asarray(bytearray(response.content), dtype="uint8")
        img = cv.imdecode(image_array, cv.IMREAD_COLOR)
        return img, file_id, file_timestamp, image_extension


# print(read_json(body))

# zdj, file_id, file_timestamp, image_extension = read_json(body)

# print(f'id: {file_id},timestamp: {file_timestamp}, rozszeżenie: {image_extension}')


def people_detection(img):
    rows = img.shape[0]
    cols = img.shape[1]
    cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
    cvOut = cvNet.forward()

    count = 0
    for detection in cvOut[0, 0, :, :]:
        classId = int(detection[1])
        score = float(detection[2])
        if classId == 1 and score > 0.4:  # Class ID 1 corresponds to 'person'
            count += 1
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            cv.rectangle(
                img,
                (int(left), int(top)),
                (int(right), int(bottom)),
                (255, 255, 0),
                thickness=2,
            )
    file_name = f"person_{count}.jpg"
    cv.imwrite(file_name, img)
    return f"zapisano {file_name}"


def prepare_response(json_data):
    zdj, id, add_time, img_extension = read_json(json_data)
    return people_detection(zdj)


print(prepare_response(body))
# def prepare_response(json_data):
#     zdj, id, add_time, img_extension = read_json(json_data)
#     img, count = people_detection(zdj)
#     try:
#         file_name = f"Id_{id}_person_{count}_execution_time_{round(time.time() - add_time)}sec{img_extension}"
#         success = cv.imwrite(file_name, img)
#         if success:
#             message = f"Sukces - liczba osób: {count}"
#         else:
#             message = "Nie udało się zapisać zdjęcia."
#     except Exception as e:
#         message = f"Error: {e}"

#     return message
