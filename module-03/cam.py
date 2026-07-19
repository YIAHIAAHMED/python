import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Camera open hoyni")
    exit()

while True:
    ret, frame = cam.read()

    if not ret:
        print("Frame paoa jacche na")
        break

    cv2.imshow("My Cam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()