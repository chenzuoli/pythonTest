m3u8文件转音频

```commandline
方法1：ffmpeg -i "https://svipsvip.ffzyread1.com/20240222/24496_7144fba2/index.m3u8" -c copy "output.ts"

方法2：音频合成：ffmpeg -i "live m3u8 link" -c copy -map a "output.ts"
方法3：音频分段：ffmpeg -i "live m3u8 link" -c copy -map a -f segment -segment_time 10 "out%d.ts"

方法4：ffmpeg -i xxx.m3u8 track.mp3

```