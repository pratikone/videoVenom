#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import cv2
import random
import datetime
import argparse
import numpy as np
import uploadvideo as uv
from moviepy.editor import *
import videoVimeo

def compare_image(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def GivemMeARandomNumber(count):
    return random.randrange(1,count)

def destroyAllFrames(pathOfFrames,count): 
    for i in range(1,count+1):
        pathToremove = os.path.join(pathOfFrames,'frame%d.jpg' %i)
        if os.path.isfile(pathToremove):
            os.remove(pathToremove)
    os.removedirs(pathOfFrames)
    
#Function to generate an array of frames from the video
def GenerateFrames(videoLocation,FrameDirectory):
    vidcap = cv2.VideoCapture(videoLocation) 
    success,image = vidcap.read()
    count = 1
    vidDirectory = os.path.dirname(videoLocation)

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')     
    if int(major_ver)  < 3 :
        fps = vidcap.get(cv2.cv.CV_CAP_PROP_FPS)
    else :
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        
    while (count < 200) and (success): 
        success,image = vidcap.read()
        frame_read = os.path.join(FrameDirectory,'frame%d.jpg' %count)
        cv2.imwrite(frame_read, image)     # save frame as JPEG file
        if cv2.waitKey(10) == 27:                     # exit if Escape is hit
            break
        count += 1

    cv2.destroyAllWindows()
    vidcap.release()
    return count,fps

#need for the preview window
def getFrameFromVideo( videoLocation, frameCount ) : 
    vidcap = cv2.VideoCapture(videoLocation) 
    success,image = vidcap.read()
    count = 1
    vidDirectory = os.path.dirname(videoLocation)

    while (count < frameCount) and (success): 
        success,image = vidcap.read()
        frame_read = os.path.join(vidDirectory,'frame%d.jpg' %count)
        count += 1

    cv2.imwrite(frame_read, image)     # save frame as JPEG file
    vidcap.release()
    return frame_read

#Gives an array of numbers but those numbers corresponds to unidentical frames
def GiveUnidenticalFrames(numVideos,FrameCount,FrameDirectory):
    RandomFrame = []
    RandomFrameData = GivemMeARandomNumber(FrameCount)
    RandomFrame.append(RandomFrameData)
    i = 1
    UNIDENTICAL_THRESHOLD = 2000
    counter_for_loop = 300
    if numVideos == 1:
        return RandomFrame
    else:
        while (i<numVideos and counter_for_loop > 0 ):
            print "frames %d counter_for_loop %d" % (i, counter_for_loop)
            Match = False
            RandomFrameData = GivemMeARandomNumber(FrameCount)
            for imgNum in range(0,len(RandomFrame)):
                imgA = cv2.imread(os.path.join(FrameDirectory,'frame%d.jpg' %RandomFrame[imgNum]))
                imgB = cv2.imread(os.path.join(FrameDirectory,'frame%d.jpg' %RandomFrameData))
                mse = compare_image(imgA,imgB)
                if mse < UNIDENTICAL_THRESHOLD:
                    Match = True
                    break
            if(Match is False):
                RandomFrame.append(RandomFrameData)
                i = i+1

            counter_for_loop = counter_for_loop - 1

        if counter_for_loop <= 0 : #when loop is stopeed abruptly and we need to fill up the list
             while len(RandomFrame) < numVideos :
                RandomFrameData = GivemMeARandomNumber(FrameCount)
                RandomFrame.append(RandomFrameData)

    return RandomFrame

#Call upload to upload the videos
def upload(youtubeObj, VidLocation,titleVid,description,tags,category='22',privacy='private'): #keywords are string of tags separated by commas, description is also a string
    if youtubeObj is None :
        return
    #Look at the auth params if there is a trouble
    args = argparse.Namespace(file=VidLocation,title=titleVid,description=description,keywords= ",".join(tags), category=category,privacyStatus=privacy,auth_host_name='localhost', auth_host_port=[8080, 8090],logging_level='ERROR', noauth_local_webserver=False)
    # youtubeObj = uv.authenticateWithYoutube(args)
    uv.uploadMyVideo( youtubeObj, args )


def uploadVimeo(vimeoObj, VidLocation,titleVid,description,tags,category='22',privacy='private'): #keywords are string of tags separated by commas, description is also a string
    if vimeoObj is None :
        return
    videoVimeo.upload(vimeoObj, VidLocation,titleVid, description, tags)

    


def GenerateTheVideo(caller, videoLocation, numVideos=1, tags = None, t1=0, t2=0, x=0, y=0, ImageLocation=None, callback = None ):
    vidDirectory = os.path.dirname(videoLocation)
    #Make directory where you put all images
    FrameDirectory = os.path.join(vidDirectory,'Frames')
    if not os.path.exists(FrameDirectory):
        os.makedirs(FrameDirectory)
    FrameCount,frame_rate = GenerateFrames(videoLocation,FrameDirectory)
    RandomFrame = GiveUnidenticalFrames(numVideos,FrameCount,FrameDirectory)
    durationOfImage = GivemMeARandomNumber(5)

    for numVideo_i in range(0,numVideos): 
        if callback is not None:
            callback( numVideo_i )
        else :
            print "No callback"
        if ImageLocation is not None :
            OverlayImage = ImageLocation #Location Of Image/Banner
            ovrImgClip = ImageClip(OverlayImage,duration=t2-t1) #Create a clip for the duration start
        
        frame_to_use = os.path.join(FrameDirectory,'frame%d.jpg' %RandomFrame[numVideo_i])
        clip1 = ImageClip(frame_to_use,duration=durationOfImage)
        clip2 = VideoFileClip(videoLocation)
        if ImageLocation is not None :
            Video = CompositeVideoClip([clip1,clip2.set_start(durationOfImage).crossfadein(1), \
                    ovrImgClip.set_start(t1+durationOfImage).set_pos((x,y))]) #Overlay the video
        else :
            Video = CompositeVideoClip([clip1,clip2.set_start(durationOfImage).crossfadein(1)]) #Overlay the video            
        if tags is not None :
            video_name = tags[numVideo_i] + ".mp4"
        else : 
            video_name = "video" + ".mp4"

        newFileLocation = os.path.join(vidDirectory,video_name)
        
        Video.write_videofile(newFileLocation,fps=frame_rate)
        if caller is not None :        
            upload( caller.youtubeObj, VidLocation =newFileLocation ,titleVid = video_name, description = video_name, tags=tags, category='22',privacy='public' )
            uploadVimeo(caller.vimeoObj, VidLocation =newFileLocation ,titleVid = video_name, description = video_name, tags=tags)


    destroyAllFrames(FrameDirectory,FrameCount)



if __name__ == "__main__":
    # main()
    print datetime.datetime.now()
    GenerateTheVideo(None, "C:/Users/pratika/Desktop/valve.avi", 2 ) #path where the video is located
    print datetime.datetime.now()


