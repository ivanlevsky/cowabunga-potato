from opencv.cvutils import *

import os
videoInput = os.path.dirname(os.getcwd()) +r'\test video\video1.mp4'
videoOutput = os.path.dirname(os.getcwd())+r'\test video\videoout.mp4'

# write video not working now
play_and_save_Video(videoInput,videoOutput, 1 ,1)



