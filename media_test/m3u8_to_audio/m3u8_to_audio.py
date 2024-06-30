"""
前提条件: 安装了ffmpeg
"""

import subprocess

# link = 'https://cs9-9v4.vkuseraudio.net/s/v1/ac/NeMmHNX2Iyt08MZ4z5fELAMybgSNR6T1xYEcBEv5Kdsenci3KHOAC-1fKapAV9vxwVOBIik40I4DwfrN-a_jtjILYVcx3mLTNCzKo1UF-UhbKOztLrboF9NEn1jzZs1Jl0ijfmccog6aAcB4PcdnrxPzXY7WCMVWtUjWKOgHad5a-g0/index.m3u8'
link = 'https://svipsvip.ffzyread1.com/20240222/24496_7144fba2/index.m3u8'
subprocess.run(['ffmpeg', '-i', link, 'track.mp3'])

