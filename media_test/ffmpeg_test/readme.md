如何制作m3u8视频流媒体文件，可以在html页面上播放：

```commandline
ffmpeg -i video_subclip.mp4 -vcodec copy -acodec copy -bsf:v h264_mp4toannexb -hls_time 10 -hls_list_size 0 -f hls m3u8/video.m3u8
```