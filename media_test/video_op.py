"""
pip install moviepy
"""

from moviepy.editor import VideoFileClip


def convert_video_format(input_video_path, output_video_path):
    video_clip = VideoFileClip(input_video_path)
    video_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')


# 使用函数转换视频格式
convert_video_format('Italian.wmv', 'Italian.avi')
