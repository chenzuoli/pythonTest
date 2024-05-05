# 安装
```bash
pip3.8 install setuptools-rust
pip3.8 install openai-whisper
or
yum install git -y
pip3 install git+https://github.com/openai/whisper.git 

whisper需求python >= 3.8
```

# 命令行测试
```commandline
whisper test.mp3 --model medium
```

其中 “test.mp3” 是我测试用的音频文件。

“--model medium” 是指定使用 medium 版本的模型（Whisper 有多种模型：tiny、base、small、medium、large，模型大小依次变大）。

第一次运行时，会先下载指定的模型，需要耐心等待一会儿。

模型下载之后，就会开始执行语音识别，输出识别结果。

并且会自动写入文件：test.txt

开源地址：http://github.com/openai/whisper



问题：
1.     ModuleNotFoundError: No module named '_ctypes'
yum install libffi-devel -y
然后重新编译安装python：
make && make altinstall