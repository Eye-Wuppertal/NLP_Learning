遇事不决，Deep Learning ，硬train一发

主要使用的六个模型

- 输入：语音    输出：文字 —— 语音辨识

- 输入：文字    输出：语音 —— 语音合成

- 输入：语音    输出：语音 —— 语音转换

- 输入：文字    输出：文字 —— 

- 输入：语音    输出：对象 —— Speaker Recognition 、Keyword Spotting

- 输入：文字    输出：对象 —— 

  

Traditional Speech Recognition

![image-20220418152812349](img/image-20220418152812349.png)

Automatic Speech Recognition 

(ASR) https://ai.googleblog.com/2019/03/an-all-neural-on-device-speech.html

![image-20220418214331701](img/image-20220418214331701.png)

| 模块名称     | 主要内容                                                     | 案例                             |
| ------------ | ------------------------------------------------------------ | -------------------------------- |
| 文本预处理   | 文本处理基本方法, 文本张量表示, 文本数据分析, 文本增强方法等 | 路透社新闻类型分类任务           |
| 经典序列模型 | HMM与CRF模型的作用, 使用过程, 差异比较以及发展现状等         |                                  |
| RNN及其变体  | RNN, LSTM, GRU模型的作用, 构建, 优劣势比较等                 | 全球人名分类任务, 英译法翻译任务 |
| Transformer  | Transformer模型的作用, 细节原理解析, 模型构建过程等          | 构建基于Transformer的语言模型    |
| 迁移学习     | fasttext工具的作用, 迁移学习理论, NLP标准数据集和预训练模型的使用等 | 全国酒店评论情感分析任务         |