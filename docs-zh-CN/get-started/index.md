---
comments: true
---

# 新一代 Kaldi

新一代 Kaldi 是一个开源的智能语音工具集，几乎涵盖了构建智能语音系统的方方面面。下图简单罗列了新一代 Kaldi 的项目矩阵，包括数据、训练到部署全链条。更多的项目见项目的 [github 主页](https://github.com/k2-fsa/){:target="_blank"}。 你也可以从这篇[旧文](https://mp.weixin.qq.com/s/f0vpatseghLi2piYpUpmQQ){:target="_blank"}中了解新一代 Kaldi 的起源与故事。

![](../assets/images/ngk-matrix.png)

## 特性及功能

智能语音领域包含非常多的子任务和子领域，新一代 Kaldi 目前支持语音识别(ASR)、语音合成(TTS)、关键词检测(KWS)、话音检测(VAD)、说话人识别(Speaker identification)、语种识别(Spoken language identification) 等等。其中有些提供了包含训练和部署全链路的技术，有些是基于优秀的第三方开源库做的部署支持，具体细节如下所示：

|   任务   |   训练   |  部署   |  相关文档    |
|----------|---------|---------|-------------|
| 语音识别(ASR)  | :material-check: | :material-check: |  [训练](./icefall.md) [部署](./sherpa/index.md) |
| 语音合成(TTS)  | :material-check: | :material-check: |  [训练](./sherpa/index.md) [部署](./sherpa/onnx.md) |
| 关键词(KWS)   | :material-check: | :material-check: |  [训练](./icefall.md) [部署](./sherpa/onnx.md)  |
| 话音检测(VAD) | :material-close: | :material-check: |  [部署](./sherpa/onnx.md) |
| 说话人识别(Speaker identification) | :material-close: | :material-check: |  [部署](./sherpa/onnx.md) |
| 语种识别(Spoken language identification) | :material-close: | :material-check: |  [部署](./sherpa/onnx.md) | 
