"""
pip install opencv-python
获取视频截图，每15秒截图一次

unset DYLD_LIBRARY_PATH

"""

import cv2

START_TIME = 4  # 设置开始时间(单位秒)
END_TIME = 100  # 设置结束时间(单位秒)

vidcap = cv2.VideoCapture("no_audio.mp4")  # 这里改自己的视频地址

fps = int(vidcap.get(cv2.CAP_PROP_FPS))  # 获取视频每秒的帧数
print(fps)

frameToStart = START_TIME * fps  # 开始帧 = 开始时间*帧率
print(frameToStart)
frametoStop = END_TIME * fps  # 结束帧 = 结束时间*帧率
print(frametoStop)

vidcap.set(cv2.CAP_PROP_POS_FRAMES, frameToStart)  # 设置读取的位置,从第几帧开始读取视频
print(vidcap.get(cv2.CAP_PROP_POS_FRAMES))  # 查看当前的帧数

success, image = vidcap.read()  # 获取第一帧

count = 0
while success and frametoStop >= count:
    if count % (30 * 15) == 0:  # 每15秒保存一次
        cv2.imwrite(r"pic/%s.jpg" % int(count / 375), image)  # 需要并保存的图片地址
        print('Process %dth seconds: ' % int(count / 375), success)
    success, image = vidcap.read()  # 每次读取一帧
    count += 1

print("end!")