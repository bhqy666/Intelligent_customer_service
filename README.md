# 智能客服系统

## 项目描述
本项目旨在开发一个智能客服系统，支持智能导航、智能问答和智能辅助功能。项目使用开源的 Whisper 模型作为自动语音识别（ASR）模块，结合 Open-webui 前端界面，实现用户通过网页前端点击按钮进行语音输入，并将语音转换为文本在前端展示。未来将进一步集成更多的智能客服功能，如自动回答和智能帮助。

## 开发计划
### 阶段 1: Whisper ASR 与前端交互
实现网页前端录音并将音频传递到后端。
后端调用 Whisper 模型进行语音转文本处理。
前端展示 Whisper 模型的文本输出。
### 阶段 2: 智能导航功能
集成简单的菜单或路径导航功能，基于用户输入进行导航。
### 阶段 3: 智能问答功能
使用开源 NLP 模型（如 GPT 等）集成智能问答功能，能够根据用户的问题给出相应答案。
### 阶段 4: 智能辅助功能
通过语音输入获取用户需求，并提供智能辅助操作，如查询数据库或执行简单任务。

## ***项目结构***
```
/intelligent-customer-service
│
├── /frontend               # 前端项目目录
│   ├── index.html          # 主网页文件
│   ├── app.js              # 处理音频录制与后端交互的 JS 文件
│   ├── styles.css          # 页面样式文件
│   └── /assets             # 静态资源
│
├── /backend                # 后端项目目录
│   ├── app.py              # 后端服务文件，处理音频上传和调用 Whisper 模型
│   ├── whisper_service.py  # Whisper 模型处理模块
│   └── /uploads            # 上传的音频文件存储目录
├── requirements.txt    # Python 依赖库列表
└── README.md               # 项目说明文件
```
## Todo List
### 阶段 1: Whisper ASR 模块与前端交互
* -[x] 搭建基本前端录音功能，使用 MediaRecorder API 进行音频录制。
* -[ ] 搭建后端 API 接收音频数据。
* -[ ] Whisper 模型部署并实现音频转文本功能。
* -[ ] 前端展示文本输出。
### 阶段 2: 智能导航
* -[ ] 设计简单的导航菜单或对话框系统。
* -[ ] 根据用户输入（语音/文本）实现动态导航。
### 阶段 3: 智能问答功能
* -[ ] 集成 NLP 问答模型。
* -[ ] 实现问答匹配与响应功能。
### 阶段 4: 智能辅助功能
* -[ ] 设计智能辅助模块，提供查询、信息反馈等功能。

## 开发要求
* 编程语言：Python (后端), JavaScript (前端)
* 前端框架：Open-webui 或原生 HTML/CSS/JavaScript
* 后端框架：Flask 或 FastAPI
* 依赖库：
  * `whisper` (语音识别模型)
  * `Flask` (或 `FastAPI` 用于 `API` 构建)
  * `mediaDevices` API（用于前端录音）

## 使用指南
### 前提条件
* 安装 Python 3.8+
* 安装必要的 Python 依赖：
```commandline
pip install -r requirements.txt
```
### 运行后端
1. 克隆项目：
```
git clone https://github.com/your-username/intelligent-customer-service.git
cd intelligent-customer-service
```

2. 启动后端 Flask 服务器：
```commandline
cd backend
python app.py
```
### 运行前端
打开 `frontend/index.html` 文件，在浏览器中运行前端页面。
点击录音按钮，进行语音输入并查看结果。

## 参考项目
* [`OpenAI Whisper`](https://github.com/openai/whisper) - 用于自动语音识别的开源模型。
* [`Open-webui`](https://github.com/open-webui/open-webui) - 用于快速搭建前端界面的开源工具。
* [`Flask`](https://github.com/pallets/flask) - 轻量级 Python 后端框架，用于构建 RESTful API。

## 贡献指南
如果你对本项目有改进建议或想要贡献代码，请提交 **Pull Request** 或 **Issue**。我们鼓励社区参与，共同完善项目。