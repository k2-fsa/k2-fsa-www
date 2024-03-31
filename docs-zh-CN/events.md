---
comments: true
title: 新一代 Kaldi 历程
---

## 2024 年

### 3月

#### icefall

- 增加基于 openfst 的 CTC 流式 HLG 解码。[代码](https://github.com/k2-fsa/icefall/pull/1557){:target="_blank"}
- 增加广东话 recipe，zipformer 模型，使用 [MDCC](https://arxiv.org/pdf/2201.02419.pdf){:target="_blank"} 数据集。[代码](https://github.com/k2-fsa/icefall/pull/1537){:target="_blank"} [模型](https://huggingface.co/zrjin/icefall-asr-mdcc-zipformer-2024-03-11/){:target="_blank"}
- 增加使用 [LoRA](https://arxiv.org/abs/2106.09685){:target="_blank"} 微调的 recipe。[代码](https://github.com/k2-fsa/icefall/pull/1540){:target="_blank"}
- 增加使用 [adapter](https://arxiv.org/pdf/1902.00751.pdf){:target="_blank"} 微调的 recipe。[代码](https://github.com/k2-fsa/icefall/pull/1512){:target="_blank"} [文档](https://k2-fsa.github.io/icefall/recipes/Finetune/adapter/finetune_adapter.html){:target="_blank"}
- 增加使用预训练 zipformer 做微调的 recipe。[代码](https://github.com/k2-fsa/icefall/pull/1484){:target="_blank"} [文档](https://k2-fsa.github.io/icefall/recipes/Finetune/from_supervised/finetune_zipformer.html){:target="_blank"}
- 增加使用 wenetspeech 和 multi-zh-han 数据集微调 whisper 模型的 recipe。 [代码](https://github.com/k2-fsa/icefall/pull/1483){:target="_blank"}

#### sherpa

- sherpa-onnx 支持语言识别(spoken language identification), 使用 whisper 实现。 [huggingface space](https://huggingface.co/spaces/k2-fsa/spoken-language-identification){:target="_blank"}
- sherpa-onnx 支持 RISC-V 平台。
- sherpa-onnx kws 支持 python、c API 和 webassembly。 
- sherpa-ncnn 支持 android wear demo。[代码](https://github.com/k2-fsa/sherpa-ncnn/pull/319){:target="_blank"} [演示视频](https://www.bilibili.com/video/BV1qS421w7cK/){:target="_blank"}
- sherap 增加 Whisper TensorRT-LLM 推理支持。[代码](https://github.com/k2-fsa/sherpa/pull/551){:target="_blank"}
