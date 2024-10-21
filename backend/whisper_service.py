import sys
sys.path.append('whisper')  # 将子模块添加到 Python 路径
import whisper

# 加载 Whisper 模型
model = whisper.load_model("base")

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result['text']

print(transcribe_audio('audio.wav'))