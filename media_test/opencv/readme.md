1. 通过opencv库进行视频的剪切
2. 获取帧图

"""
pip install opencv-python==4.8.1.78
"""

echo $DYLD_LIBRARY_PATH
/opt/X11/lib:/Users/zuolichen/opt/software/ImageMagick-7.0.10/lib/


运行前：
```commandline
unset DYLD_LIBRARY_PATH
```

# error
1. macos bigsur 11
ImportError: dlopen(/Users/zuolichen/PycharmProjects/pythonProject/venv/lib/python3.8/site-packages/cv2/cv2.abi3.so, 2): Symbol not found: _CGLGetCurrentContext
  Referenced from: /System/Library/Frameworks/OpenCL.framework/Versions/A/OpenCL
  Expected in: /System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL
 in /System/Library/Frameworks/OpenCL.framework/Versions/A/OpenCL

solation:
unset DYLD_LIBRARY_PATH