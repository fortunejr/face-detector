import cv2
# Note: Images should all be in Black and White
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('b&w faces/download (6).jpg')

webcam = cv2.VideoCapture('me2.mp4')

while True:
    successful_frame_img, frame = webcam.read()

    greyscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Clever Programmer Face Detector', frame)
    face_coordinates = trained_face_data.detectMultiScale(greyscale_img)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
        print('Code Completed')

webcam.release()