---
title: Pre-trained Keyword spotting models
comments: true
---

# Keyword spotting models

Currently, we offer two basic models in Chinese and English, both supporting the Pytorch and onnxruntime frameworks. The Pytorch model is mainly used for fine-tuning, while the onnx model is mainly used for deployment. You can first use onnx models to test the performance of the target keywords. If the expected results are not achieved, then consider fine-tuning based on the basic model we provide. 


|   Language  |   Framework   |  Download link   |   Usage   |   Description   |
|---------|-------------|------------|--------------|--------------|
| Chinese  | Pytorch  | [github](https://github.com/pkufool/keyword-spotting-models/releases/download/v0.11/icefall-kws-zipformer-wenetspeech-20240219.tar.gz) | [Training and Fine-tuning](https://github.com/k2-fsa/icefall/pull/1428){:target="_blank"}  | This model is trained on Wenetspeech L (10,000 hours), with a model parameter of about 3.3M. The modeling units are pinyin (initials and finals), and can be used as a basic model for fine-tuning. |
| Chinese  | onnxruntime | [github](https://github.com/pkufool/keyword-spotting-models/releases/download/v0.1/sherpa-onnx-kws-zipformer-wenetspeech-3.3M-2024-01-01.tar.bz) | [Deployment docs](https://k2-fsa.github.io/sherpa/onnx/kws/pretrained_models/index.html#sherpa-onnx-kws-zipformer-wenetspeech-3-3m-2024-01-01-chinese){:target="_blank"} | This model is exported from the model above，could be used for deployment on [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx){:target="_blank"} |
| English  | Pytorch  | [github](https://github.com/pkufool/keyword-spotting-models/releases/download/v0.11/icefall-kws-zipformer-gigaspeech-20240219.tar.gz) | [Training and Fine-tuning](https://github.com/k2-fsa/icefall/pull/1428){:target="_blank"}  | This model is trained on Gigaspeech XL (10,000 hours), with a model parameter of about 3.3M. The modeling units are BPEs, and can be used as a basic model for fine-tuning. |
| English  | onnxruntime | [github](https://github.com/pkufool/keyword-spotting-models/releases/download/v0.1/sherpa-onnx-kws-zipformer-gigaspeech-3.3M-2024-01-01.tar.bz) | [Deployment docs](https://k2-fsa.github.io/sherpa/onnx/kws/pretrained_models/index.html#sherpa-onnx-kws-zipformer-gigaspeech-3-3m-2024-01-01-english){:target="_blank"} | This model is exported from the model above，could be used for deployment on [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx){:target="_blank"}  |

