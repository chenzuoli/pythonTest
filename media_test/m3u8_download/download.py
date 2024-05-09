"""
pip install m3u8-To-MP4==0.1.11
"""

import m3u8_To_MP4

if __name__ == '__main__':
    # 1. Download videos from uri.
    # m3u8_To_MP4.multithread_download('https://svipsvip.ffzyread1.com/20240424/26411_4538b0e5/index.m3u8')
    m3u8_To_MP4.multithread_download('https://v5.tlkqc.com/wjv5/202405/04/LsJM6rsQ0p77/video/index.m3u8')

    # 2. Download videos from existing m3u8 files.
    # m3u8_file_path = '/Users/zuolichen/Downloads/index.m3u8'
    # m3u8_To_MP4.multithread_file_download('https://svipsvip.ffzyread1.com/20240424/26411_4538b0e5/index.m3u8', m3u8_file_path)

    # For compatibility, i reserve this api, but i do not recommend to you again.
    # m3u8_To_MP4.download('http://videoserver.com/playlist.m3u8')
