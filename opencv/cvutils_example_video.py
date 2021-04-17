from opencv.cvutils import *
from python_common.global_param import GlobalParam


# write video not working now, need resize frame before write video file
play_and_save_Video(GlobalParam.get_video_input(), GlobalParam.get_video_output(), 1 ,1)

# screen record show opencv window and write video file
screen_record(0, 0, 2560, 1600, 'avc1', 'mp4', 10, 0.5)

# screen record not show opencv window and write video file use timeout
screen_record(0, 0, 640, 400, 'avc1', 'mp4', 10, 0.5, 30)

# screen record show opencv window and write video file use screen offset
screen_record(100, 200, 640, 400, 'avc1', 'mp4', 10, 0.5)



