# TODO
# function source: "https://stackoverflow.com/questions/46864915/python-add-audio-to-video-opencv"

import cv2
from ffpyplayer.player import MediaPlayer

video_path="res/Megamind.avi"
fps = 34

def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(fps) & 0xFF == ord("q"):
            break

        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audioq
            img, t = audio_frame

    video.release()
    cv2.destroyAllWindows()

PlayVideo(video_path)
