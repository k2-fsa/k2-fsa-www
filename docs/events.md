---
comments: true
title: Events for Next-gen Kaldi
---

## 2024

### March

#### icefall

- Add HLG decoding for streaming CTC (based on openfst). [code](https://github.com/k2-fsa/icefall/pull/1557){:target="_blank"}
- Add zipformer Cantonese recipe, using [MDCC](https://arxiv.org/pdf/2201.02419.pdf){:target="_blank"} dataset. [code](https://github.com/k2-fsa/icefall/pull/1537){:target="_blank"} [model](https://huggingface.co/zrjin/icefall-asr-mdcc-zipformer-2024-03-11/){:target="_blank"}
- Add finetuing recipe using [LoRA](https://arxiv.org/abs/2106.09685){:target="_blank"}. [code](https://github.com/k2-fsa/icefall/pull/1540){:target="_blank"}
- Add finetuing recipe using [adapter](https://arxiv.org/pdf/1902.00751.pdf){:target="_blank"}. [code](https://github.com/k2-fsa/icefall/pull/1512){:target="_blank"} [Doc](https://k2-fsa.github.io/icefall/recipes/Finetune/adapter/finetune_adapter.html){:target="_blank"}
- Add finetuing recipe using pre-trained zipformer model. [code](https://github.com/k2-fsa/icefall/pull/1484){:target="_blank"} [Doc](https://k2-fsa.github.io/icefall/recipes/Finetune/from_supervised/finetune_zipformer.html){:target="_blank"}
- Finetuing whisper using Wenetspeech & multi-zh-han dataset. [code](https://github.com/k2-fsa/icefall/pull/1483){:target="_blank"}

#### sherpa

- Add spoken language identification support (based on whisper) in sherpa-onnx. [huggingface space](https://huggingface.co/spaces/k2-fsa/spoken-language-identification){:target="_blank"}
- Add RISC-V support in sherpa-onnx。
- Add python、c API and webassembly support for keyword spotting task in sherpa-onnx.
- Add android wear demo in sherpa-ncnn。[code](https://github.com/k2-fsa/sherpa-ncnn/pull/319){:target="_blank"} [video](https://www.bilibili.com/video/BV1qS421w7cK/){:target="_blank"}
- Inference Whisper using TensorRT-LLM in sherpa. [code](https://github.com/k2-fsa/sherpa/pull/551){:target="_blank"}
