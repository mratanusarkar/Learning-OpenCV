import cv2
import math
import numpy as np

cap = cv2.VideoCapture("../res/vtest.avi")
fps = 40

grabbed, frame1 = cap.read()
grabbed, frame2 = cap.read()


def distance(rectangle_1, rectangle_2):
    x1, y1, w1, h1 = rectangle_1
    x2, y2, w2, h2 = rectangle_2
    x1_cm = x1 + w1 / 2
    y1_cm = y1 + h1 / 2
    x2_cm = x2 + w2 / 2
    y2_cm = y2 + h2 / 2
    return math.sqrt((x2_cm - x1_cm)**2 + (y2_cm - y1_cm)**2)


# TODO
def merge_nearby_rectangles(rectangles, max_distance):
    merged_rectangles = []
    for i in range(len(rectangles)-1):
        append_count = 0
        for j in range(i, len(rectangles)):
            if distance(rectangles[i], rectangles[j]) < max_distance:
                x_new = min(rectangles[i][0], rectangles[j][0])
                y_new = min(rectangles[i][1], rectangles[j][1])
                w_new = max(rectangles[i][0], rectangles[j][0]) - min(rectangles[i][0], rectangles[j][0])
                h_new = max(rectangles[i][1], rectangles[j][1]) - min(rectangles[i][1], rectangles[j][1])
                merged_rectangles.append((x_new, y_new, w_new, h_new))
                append_count += 1
        # if no close rectangles found close ti the ith rect, preserve this lonely rect!
        if append_count == 0:
            merged_rectangles.append(rectangles[i])

    # remove duplicates if any and return the list of new rectangles
    return list(set(merged_rectangles))


while cap.isOpened():

    if not grabbed:
        print("End of Video")
        break
    if cv2.waitKey(fps) == 27:
        break

    # all code to work with the frame goes here
    diff = cv2.absdiff(frame2, frame1)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, binary = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, None, iterations=2)
    dilate = cv2.dilate(opening, None, iterations=5)    # made for now, =2/3 after TODO

    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1, contours, -1, (0, 0, 255), 1)
    valid_bounds = []     # TODO

    for contour in contours:
        # ignore small contours
        if cv2.contourArea(contour) < 100:  # 50 after TODO
            continue

        # get all bounding rectangles
        (x, y, width, height) = cv2.boundingRect(contour)

        # height should be > width for it to be a person
        if (height / width) <= 1:
            continue

        valid_bounds.append((x, y, width, height))

    # valid_bounds = merge_nearby_rectangles(valid_bounds, 50)  # TODO

    for (x, y, width, height) in valid_bounds:
        cv2.rectangle(frame1, (x, y), (x + width, y + height), (0, 255, 0), 2)

    # output frame, read next frame and swap
    cv2.imshow('feed', frame1)
    frame1 = frame2
    grabbed, frame2 = cap.read()

cap.release()
cv2.destroyAllWindows()
