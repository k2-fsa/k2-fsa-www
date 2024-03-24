---
comments: true
title: 语音识别演示
---

新一代 Kaldi 不仅提供语音识别[模型训练](https://github.com/k2-fsa/icefall){:target="_blank"}和[部署](https://github.com/k2-fsa/sherpa-onnx){:target="_blank"}的方案，我们还发布了众多的预训练模型和相应的演示程序，供广大开发者体验学习。

## Huggingface space

体验新一代 Kaldi 最直接最便捷的方式是用浏览器访问我们提供的 Huggingface space，目前支持包括中文、英文、中英文、中英粤、粤语、藏语、阿拉伯语、德语、法语、俄语等语言数十个个模型的体验。

体验地址[huggingface :hugging:](https://huggingface.co/spaces/k2-fsa/automatic-speech-recognition){:target="_blank"}。
> 对于大陆用户，如无法访问 huggingface，可以使用 [hf-mirror :hugging:](https://hf-mirror.com/spaces/k2-fsa/automatic-speech-recognition){:target="_blank"} 体验。

[![](../assets/images/asr_huggingface.png "新一代 Kaldi huggingface 语音识别空间")](https://huggingface.co/spaces/k2-fsa/automatic-speech-recognition){:target="_blank"}

### Webassembly

新一代 Kaldi 还提供了 [webassembly](https://webassembly.org/){:target="_blank"} 支持，将模型的推理和解码完全迁移到浏览器端，不需花费服务器的计算资源。我们提供了如下一些模型的体验地址，如果你想用 webassembly 打包自己的模型，可以参考 [sherpa-onnx 文档](https://k2-fsa.github.io/sherpa/onnx/wasm/index.html)和 [sherpa-ncnn 文档](https://k2-fsa.github.io/sherpa/ncnn/wasm/index.html)。

| 语言 | 声学编码器 | 引擎 | 体验地址 | 模型地址 |
|------|-----|-----|-----|-----|
|  英文   |   zipformer        |  onnxruntime   |  [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-onnx-en){:target="_blank"} [modelscope](https://modelscope.cn/studios/k2-fsa/web-assembly-asr-sherpa-onnx-en/summary){:target="_blank"}      | [模型文档](https://k2-fsa.github.io/sherpa/onnx/pretrained_models/online-transducer/zipformer-transducer-models.html#csukuangfj-sherpa-onnx-streaming-zipformer-en-2023-06-21-english){:target="_blank"}    |
|  中英文   |   zipformer        |  onnxruntime   |  [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-onnx-zh-en){:target="_blank"} [modelscope](https://modelscope.cn/studios/k2-fsa/web-assembly-asr-sherpa-onnx-zh-en/summary){:target="_blank"}      | [模型文档](https://k2-fsa.github.io/sherpa/onnx/pretrained_models/online-transducer/zipformer-transducer-models.html#csukuangfj-sherpa-onnx-streaming-zipformer-bilingual-zh-en-2023-02-20-bilingual-chinese-english){:target="_blank"}    |
|  中英文   |   paraformer        |  onnxruntime   |  [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-onnx-zh-en-paraformer){:target="_blank"} [modelscope](https://modelscope.cn/studios/k2-fsa/web-assembly-asr-sherpa-onnx-zh-en-paraformer/summary){:target="_blank"}      | [模型文档](https://k2-fsa.github.io/sherpa/onnx/pretrained_models/online-paraformer/paraformer-models.html#csukuangfj-sherpa-onnx-streaming-paraformer-bilingual-zh-en-chinese-english){:target="_blank"}    |
|  中英粤(方言)   |   paraformer        |  onnxruntime   |  [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-onnx-zh-cantonese-en-paraformer){:target="_blank"} [modelscope](https://modelscope.cn/studios/k2-fsa/web-assembly-asr-sherpa-onnx-zh-cantonese-en-paraformer/summary){:target="_blank"}      | [模型文档](https://k2-fsa.github.io/sherpa/onnx/pretrained_models/online-paraformer/paraformer-models.html#csukuangfj-sherpa-onnx-streaming-paraformer-trilingual-zh-cantonese-en-chinese-cantonese-english){:target="_blank"}    |
|  英文   |   zipformer        |  ncnn   |  [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-ncnn-en){:target="_blank"} [modelscope](https://modelscope.cn/studios/k2-fsa/web-assembly-asr-sherpa-ncnn-en/summary){:target="_blank"}      | [模型文档](https://k2-fsa.github.io/sherpa/ncnn/pretrained_models/zipformer-transucer-models.html#csukuangfj-sherpa-ncnn-streaming-zipformer-en-2023-02-13-english){:target="_blank"}    |
|  中英文   |   zipformer        |  ncnn   |  [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-ncnn-zh-en){:target="_blank"} [modelscope](https://modelscope.cn/studios/k2-fsa/web-assembly-asr-sherpa-ncnn-zh-en/summary){:target="_blank"}      | [模型文档](https://k2-fsa.github.io/sherpa/ncnn/pretrained_models/zipformer-transucer-models.html#csukuangfj-sherpa-ncnn-streaming-zipformer-bilingual-zh-en-2023-02-13-bilingual-chinese-english){:target="_blank"}    |


### 视频字幕提取

字幕提取功能是我们基于语音识别制作的一个小工具，用户只需上传视频即可生成对应的字幕文件，中文、英文、中英文、俄语体验地址：[Huggingface :hugging:](https://huggingface.co/spaces/k2-fsa/generate-subtitles-for-videos){:target="_blank"}, [Huggingface 镜像站](https://hf-mirror.com/spaces/k2-fsa/generate-subtitles-for-videos){:target="_blank"}。


## 视频

为了便于大家快速看到演示的效果，我们还制作了很多视频供大家预览，请移步[:fontawesome-brands-bilibili: Bilibili](https://space.bilibili.com/1234519871/video?tid=0&special_type=&pn=1&keyword=&order=click){:target="_blank"}自行选择阅看。


## apk & exe

我们同样提供了一些编译好的安卓 APK 和 Windows 可执行程序，大家自行下载安装即可试用。

| 语言 | 引擎 | 平台 | 下载地址 |
|----|----|----|----|
| 中文 | onnxruntime | 安卓 | [链接](../resources.md?s=onnx.*[x86\|x86_64\|arm]-zh.apk){:target="_blank"}  |
| 英文 | onnxrumtime | 安卓 | [链接](../resources.md?s=onnx.*[x86\|x86_64\|arm]-en.apk){:target="_blank"} |
| 中英文 | onnxrumtime | 安卓 | [链接](../resources.md?s=onnx.*[x86\|x86_64\|arm]-bilingual.*apk){:target="_blank"} |
| 中英文 | ncnn | 安卓 | [链接](../resources.md?s=ncnn.*[x86\|x86_64\|arm]-bilingual.*apk){:target="_blank"} |
| 全语言(自行下载模型)   | onnxruntime | Windows | [链接](../resources.md?s=asr.*exe){:target="_blank"} |
| 全语言(自行下载模型)   | ncnn | Windows | [链接](../resources.md?s=ncnn.*exe){:target="_blank"} |
