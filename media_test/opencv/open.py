"""
剪切视频

error:
macos bigsur 11
opencv Symbol not found: _CGLGetCurrentContext   Referenced from

pip install opencv-python==4.8.1.78

"""

import cv2

# 设置要剪切的视频路径和输出路径
input_path = '无音频.mp4'
output_path = 'output.mp4'

# 设置要剪切的开始时间和结束时间（秒）
start = 10  # 从第10秒开始
end = 20  # 到第20秒结束

# 创建VideoCapture对象
cap = cv2.VideoCapture(input_path)

# 获取视频的编码格式和帧率
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建VideoWriter对象来写入剪切后的视频
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# 读取视频帧并写入剪切后的视频
current_frame = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    current_frame += 1
    if start <= current_frame <= end:
        out.write(frame)

    if current_frame > end:
        break

# 释放VideoCapture和VideoWriter对象
cap.release()
out.release()
