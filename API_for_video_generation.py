import cv2
from moviepy.editor import *
from PIL import *
import os
import random

def GivemMeARandomNumber(count):
    return random.randrange(1,count)


def destroyAllFrames(pathOfVideo): 
    for i in range(1,count+1):
        pathToremove = os.path.join(pathOfVideo,'frame%d.jpg' %i)
        if os.path.isfile(pathToremove):
            os.remove(pathToremove)

def GenerateTheVideo(pathOfVideo,durationOfImage, numVideos=1):
    videoLocation = os.path.join(pathOfVideo,'test.avi') #Locate the video
    vidcap = cv2.VideoCapture(videoLocation) 
    success,image = vidcap.read()
    count = 1

    while success:
        success,image = vidcap.read()
        frame_read = os.path.join(pathOfVideo,'frame%d.jpg' %count)
        cv2.imwrite(frame_read, image)     # save frame as JPEG file
        if cv2.waitKey(10) == 27:                     # exit if Escape is hit
            break
        count += 1

    RandomFrame = []
    RandomFrameData = GivemMeARandomNumber(count)
    for numVideo_i in range(0,numVideos): 
        while RandomFrameData in RandomFrame:
            RandomFrameData = GivemMeARandomNumber(count)

        RandomFrame.append(RandomFrameData)
        frame_to_use = os.path.join(pathOfVideo,'frame%d.jpg' %RandomFrame[numVideo_i])
        clip1 = ImageClip(frame_to_use, duration = GivemMeARandomNumber(5))
        clip2 = VideoFileClip(videoLocation)
        Video = CompositeVideoClip([clip1,clip2.set_start(durationOfImage).crossfadein(1)])
        newFileLocation = os.path.join(pathOfVideo,'new_video_kind%d.mp4' %RandomFrame[numVideo_i])
        Video.write_videofile(newFileLocation,fps=25)
    
    cv2.destroyAllWindows()
    vidcap.release()

    destroyAllFrames(pathOfVideo)


GenerateTheVideo("C:\/Python27\/codes\/opencv tut",2,2) #path where the video is located
