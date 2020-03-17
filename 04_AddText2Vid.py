import cv2
import datetime

cap = cv2.VideoCapture("res/Megamind.avi")

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 720p = 1280 x 720, # 1080p = 1920 x 1080
cap.set(3, 1920)
cap.set(4, 1080)
print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    grabbed, frame = cap.read()

    if not grabbed:
        print("End of Video")
        break
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

    # all code to work with the frame goes here
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "Width: " + str(cap.get(3)) + " Height: " + str(cap.get(4))
    dt = str(datetime.datetime.now())
    frame = cv2.putText(frame, text, (8, 20), font, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
    frame = cv2.putText(frame, dt, (465, 520), font, 0.5, (255,0,255), 1, cv2.LINE_AA)
    cv2.imshow('output', frame)

cap.release()
cv2.destroyAllWindows()
