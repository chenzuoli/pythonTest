import whisper

"""
whisper模型还是会使用到本地的ffmpeg工具
所以本地需要安装ffmpeg
"""
# 加载模型
model = whisper.load_model("medium")

# 加载音频文件
audio = whisper.load_audio("音频.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)

