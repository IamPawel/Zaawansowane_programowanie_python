from imports import *

cvNet = cv.dnn.readNetFromTensorflow(
    "models/frozen_inference_graph.pb", "models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt"
)


def people_detection(image):
    rows = image.shape[0]
    cols = image.shape[1]
    cvNet.setInput(
        cv.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False)
    )
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
                image,
                (int(left), int(top)),
                (int(right), int(bottom)),
                (255, 255, 0),
                thickness=2,
            )
    return image, count
