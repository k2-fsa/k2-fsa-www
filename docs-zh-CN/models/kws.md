---
title: 关键词检出模型
comments: true
---

# 关键词检测模型

目前我们提供了中文和英文两个基础模型，都支持 Pytorch 和 onnxruntime 框架，Pytorch 模型主要用于微调，onnx 模型主要用于部署，可先使用 onnx 测试目标关键词的效果，如果达不到预期再考虑基于我们提供的基础模型微调。


|   语言  |   推理框架   |  下载地址   |   使用方法   |   简介   |
|---------|-------------|------------|--------------|--------------|
| 中文  | Pytorch  | [github](https://github.com/pkufool/keyword-spotting-models/releases/download/v0.11/icefall-kws-zipformer-wenetspeech-20240219.tar.gz) | [训练及微调方法](https://github.com/k2-fsa/icefall/pull/1428){:target="_blank"}  | 该模型是基于 Wenetspeech 1万小时训练，模型参数约为 3.3M，拼音（声韵母）建模，可作为基础模型用于微调。|
| 中文  | onnxruntime | [github](https://github.com/pkufool/keyword-spotting-models/releases/download/v0.1/sherpa-onnx-kws-zipformer-wenetspeech-3.3M-2024-01-01.tar.bz) [modelscope](https://www.modelscope.cn/models/pkufool/sherpa-onnx-kws-zipformer-wenetspeech-3.3M-2024-01-01/summary){:target="_blank"} | [部署教程](https://k2-fsa.github.io/sherpa/onnx/kws/pretrained_models/index.html#sherpa-onnx-kws-zipformer-wenetspeech-3-3m-2024-01-01-chinese){:target="_blank"} | 此为上述基础模型导出的 onnx，可用于 [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx){:target="_blank"} 平台部署 |
| 英文  | Pytorch  | [github](https://github.com/pkufool/keyword-spotting-models/releases/download/v0.11/icefall-kws-zipformer-gigaspeech-20240219.tar.gz) | [训练及微调方法](https://github.com/k2-fsa/icefall/pull/1428){:target="_blank"}  | 该模型是基于 Gigaspeech 1万小时训练，模型参数约为 3.3M，BPE 建模，可作为基础模型用于微调。|
| 英文  | onnxruntime | [github](https://github.com/pkufool/keyword-spotting-models/releases/download/v0.1/sherpa-onnx-kws-zipformer-gigaspeech-3.3M-2024-01-01.tar.bz) [modelscope](https://www.modelscope.cn/models/pkufool/sherpa-onnx-kws-zipformer-gigaspeech-3.3M-2024-01-01/summary){:target="_blank"} | [部署教程](https://k2-fsa.github.io/sherpa/onnx/kws/pretrained_models/index.html#sherpa-onnx-kws-zipformer-gigaspeech-3-3m-2024-01-01-english){:target="_blank"} | 此为上述基础模型导出的 onnx，可用于 [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx){:target="_blank"} 平台部署 |

> 如果上述下载链接(尤其是 github/huggingface 链接)被墙无法下载，可使用我们的提供的[下载工具](https://r.kingway.fun/k2-sync/download){:target="_blank"}下载。

