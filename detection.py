from imports import *
from detect_people import people_detection


def read_json(data):
    try:
        file_data = data.get("file")
        file_type = data.get("type")
        file_id = data.get("uuid")
        file_timestamp = data.get("timestamp")

        if file_type == "file":
            image_data = base64.b64decode(file_data)
            image = Image.open(BytesIO(image_data))
            image_extension = image.format.lower()
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
        else:
            raise ValueError("Invalid data type")
    except Exception as e:
        print(f"Error in read_json function: {e}")


def prepare_response(json_data):
    try:
        zdj, id, add_time, img_extension = read_json(json_data)
        img, count = people_detection(zdj)
        output_folder = "output_img"
        file_name = f"Id_{id}_person_{count}_execution_time_{round(time.time() - add_time)}sec.{img_extension}"
        full_path = os.path.join(output_folder, file_name)
        cv.imwrite(full_path, img)
        return count
    except Exception as e:
        print(f"Error in prepare_response function: {e}")
