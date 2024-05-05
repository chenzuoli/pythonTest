# -*- coding:utf8 -*-

import whisper


# 看看有哪些可用的模型
# models = whisper.available_models()
# print(models) ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large']

# 这个base模型识别中文准确率不太高啊
# model = whisper.load_model("base")

model = whisper.load_model("large-v3")
result = model.transcribe("audio.mp3")
for segment in result['segments']:
    print(segment['text'], segment['start'], segment['end'])

print("========")

# model = whisper.load_model("base")
# audio = whisper.load_audio('audio.mp3')
# result = model.transcribe(audio)
# for segment in result["segments"]:
#     print(segment)
