from flask import Flask
from flask_restful import Resource, Api, reqparse
from urllib.request import urlopen
import numpy as np
import cv2 as cv
import base64

from detect import people_count

app = Flask(__name__)
api = Api(app)


hello_msg = """Use /fromdrive to get people count from an image in the drive
/fromurl to get people count from an image in a URL
/frombase64 to get people count from a base64 encoded image"""



class Hello(Resource):
    def get(self):
        return hello_msg


class PeopleDetectionDrive(Resource):
    def get(self):
        img = cv.imread("input.jpg")
        count = people_count(img)
        return {"people_count": count}


class PeopleDetectionUrl(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("url", type=str, help="URL of the image")
        args = parser.parse_args()
        try:
            # Check if URL is an image
            response = urlopen(args["url"])
            mimetype = response.info().get_content_type()
            if mimetype.startswith("image"):
                # Read image from URL
                image = np.asarray(bytearray(response.read()), dtype="uint8")
                img = cv.imdecode(image, cv.IMREAD_COLOR)

                # Get people count
                count = people_count(img)
                return {"people_count": count}
            else:
                return {"error": "URL is not an image"}, 400
        except Exception as e:
            return {"error": str(e)}, 400


class PeopleDetectionBase64(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("base64", type=str, help="Base64 encoded image")
        args = parser.parse_args()
        try:
            # Remove data URI scheme
            base64_str = args["base64"].split(",")[-1]

            # Decode base64
            image_data = base64.b64decode(base64_str)
            image = np.frombuffer(image_data, np.uint8)

            # Decode image
            img = cv.imdecode(image, cv.IMREAD_COLOR)

            # Get people count
            count = people_count(img)
            return {"people_count": count}
        except Exception as e:
            return {"error": str(e)}, 400


api.add_resource(Hello, "/")
api.add_resource(PeopleDetectionDrive, "/drive")
api.add_resource(PeopleDetectionUrl, "/url")
api.add_resource(PeopleDetectionBase64, "/base64")


if __name__ == "__main__":
    app.run(debug=True)