import cv2 as cv

cvNet = cv.dnn.readNetFromTensorflow(
    "models/frozen_inference_graph.pb", "models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt"
)




def people_count(path):
    img = cv.imread(path)
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
    #cv.imwrite("output.jpg", img)
    return f'Number of people: {count}', cv.imwrite("output.jpg", img)

print(people_count("input.jpg"))