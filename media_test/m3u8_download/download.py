"""
pip install m3u8-To-MP4==0.1.11
"""

import m3u8_To_MP4

if __name__ == '__main__':
    # 1. Download videos from uri.
    # m3u8_To_MP4.multithread_download('https://svipsvip.ffzyread1.com/20240424/26411_4538b0e5/index.m3u8')
    # m3u8_To_MP4.multithread_download('https://v5.tlkqc.com/wjv5/202405/04/LsJM6rsQ0p77/video/index.m3u8')
    # m3u8_To_MP4.multithread_download('https://v11.tlkqc.com/wjv11/202407/14/HbwxbpbTnF83/video/index.m3u8')
    # 逆行人生-电影
    # m3u8_To_MP4.multithread_download('https://v4.tlkqc.com/wjv4/202410/01/xQYZ34chZm76/video/index.m3u8')
    # 小小士兵-电影
    # m3u8_To_MP4.multithread_download('https://vip.ffzy-play2.com/20240529/60101_e7c4c217/index.m3u8')
    # 过往人生-电影
    m3u8_To_MP4.multithread_download('https://vip1.lz-cdn1.com/20230822/21949_76f0f3e7/index.m3u8')
    # 黑客帝国3
    # m3u8_To_MP4.multithread_download('https://v9.qrssv.com/202408/21/mzrg1KPazE18/video/index.m3u8')


    # 2. Download videos from existing m3u8 files.
    # m3u8_file_path = '/Users/zuolichen/Downloads/index.m3u8'
    # m3u8_To_MP4.multithread_file_download('https://svipsvip.ffzyread1.com/20240424/26411_4538b0e5/index.m3u8', m3u8_file_path)

    # For compatibility, i reserve this api, but i do not recommend to you again.
    # m3u8_To_MP4.download('http://videoserver.com/playlist.m3u8')
