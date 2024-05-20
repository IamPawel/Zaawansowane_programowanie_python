import cv2 as cv
import numpy as np
import requests
import base64
import json
import time
import imghdr
import os
from detect_people import people_detection


def read_json(data):
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


def prepare_response(json_data):
    zdj, id, add_time, img_extension = read_json(json_data)
    img, count = people_detection(zdj)
    try:
        file_name = f"Id_{id}_person_{count}_execution_time_{round(time.time() - add_time)}sec{img_extension}"
        success = cv.imwrite(file_name, img)
        if success:
            message = f"Sukces - liczba osób: {count}"
        else:
            message = "Nie udało się zapisać zdjęcia."
    except Exception as e:
        message = f"Error: {e}"

    return message
