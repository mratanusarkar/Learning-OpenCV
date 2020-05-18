import cv2
import math

cap = cv2.VideoCapture("res/Megamind.avi")
fps = math.floor(cap.get(cv2.CAP_PROP_FPS))    # in ms

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (720, 528), 0)

while cap.isOpened():
    grabbed, frame = cap.read()
    
    if not grabbed:
        print("End of Video")
        break
    if cv2.waitKey(fps) & 0xFF == ord('q'):
        break
    
    # all code to work with the frame goes here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('output', gray)
    out.write(gray)

cap.release()
out.release()
cv2.destroyAllWindows()
