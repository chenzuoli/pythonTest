# -*- coding: utf8 -*-
"""
pip install moviepy -i https://pypi.mirrors.ustc.edu.cn/simple/

# imagemagic
pip install Wand
brew install imagemagick

# https://imagemagick.org/script/download.php#macosx

下载安装xquartz：https://www.xquartz.org/


下载安装ffmeg：https://ffmpeg.org/download.html
tar zxvf ffmpeg-7.0.tar.gz
cd ffmpeg-7.0
./configure --disable-x86asm
make && make install
ffmpeg -version


pip install --upgrade imageio

# 音频转文字
pip install pydub SpeechRecognition

"""
from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips
from moviepy.video.VideoClip import TextClip

video_path = "乐知付加密平台介绍.mov"


def extract_audio_from_video():
    """
    ok
    :return:
    """
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile("音频.mp3")


def add_text_to_video():
    """
    添加文字
    :return:
    """
    video = VideoFileClip(video_path).subclip(50, 60)  # 可剪切视频
    text_clip = (TextClip("My Video 2024", fontsize=70, color="white")
                 .set_position("center")
                 .set_duration(10))  # 但是添加的字幕没有看到
    result = CompositeVideoClip([video, text_clip])  # Overlay text on video
    result.write_videofile("myHolidays_edited.webm", fps=25)  # Many options...


def delete_audio_from_video():
    """
    ok
    :return:
    """
    clip = VideoFileClip(video_path)
    video = clip.without_audio()
    video.write_videofile("无音频.mp4")


def trans_audio_type():
    from pydub import AudioSegment
    audio_file = "音频.mp3"
    sound = AudioSegment.from_mp3(audio_file)
    sound.export("音频.wav", format="wav")


def trans_audio_type2():
    """
    还是需要安装ffmpeg系统工具
    :return:
    """
    from ffmpy import FFmpeg as mpy  # 音频格式转换对象
    mp3_file = "音频.mp3"
    wav_file_path = "音频.wav"
    # 创建转换时的命令行参数字符串
    cmder = '-f wav -ac 1 -ar 16000'
    # 创建转换器对象
    mpy_obj = mpy(
        inputs={
            mp3_file: None
        },
        outputs={
            wav_file_path: cmder
        }
    )
    print('执行CMDER 命令：{}'.format(mpy_obj.cmd))
    # 执行转换
    mpy_obj.run()


def extract_text_from_audio():
    """
    ValueError: Audio file could not be read as PCM WAV, AIFF/AIFF-C, or Native FLAC; check if file is corrupted or in another format
    audio格式必须是wav格式
    :return:
    """
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.AudioFile("音频.mp3") as source:
        audio_data = r.record(source)
    text = r.recognize_google_cloud(audio_data, language='zh-CN')
    print(text)


def video_subclip():
    """
    视频剪切
    :return:
    """
    # 从第8s剪切到2min12s
    subclip = VideoFileClip(video_path).subclip(t_start=8, t_end=(2, 12))

    # 剪切掉0~5s
    cutout = VideoFileClip(video_path).cutout(0, 5)

    # 拼接2段视频
    videoclips = concatenate_videoclips([subclip, cutout])

    # 创建并添加合成字幕
    text_clip = TextClip(txt="添加的字幕", fontsize=50, color="black", bg_color="transparent",
                         transparent=True).set_position(('right', 'top')).set_duration(1200).set_start(0)

    video_result = CompositeVideoClip([videoclips, text_clip])
    video_result.write_videofile("剪切及合成视频.mp4")


if __name__ == '__main__':
    # add_text_to_video()
    # extract_audio_from_video()
    # delete_audio_from_video()
    # video_subclip()
    # trans_audio_type()
    trans_audio_type2()
    # extract_text_from_audio()
