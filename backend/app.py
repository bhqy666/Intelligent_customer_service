import gradio as gr
import sys
sys.path.append('whisper')  # 将子模块添加到 Python 路径
import whisper

# 加载 Whisper 模型
model = whisper.load_model("base")

# 定义处理音频的函数
def transcribe(audio):
    # Whisper 处理音频并生成文本
    transcription = model.transcribe(audio,language='zh')["text"]
    return transcription

# 创建 Gradio 接口
interface = gr.Interface(
    fn=transcribe,  # 处理函数
    inputs=gr.Audio(type="filepath"),  # 音频输入
    outputs=gr.Textbox(),  # 文本输出
    title="智能客服 - 语音输入",
    description="点击按钮开始录音，将音频转换为文本",
)

# 启动 Gradio 界面
interface.launch()
