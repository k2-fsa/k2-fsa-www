---
comments: true
title: Demos for ASR
---

The Next-gen Kaldi not only provides solutions for [training speech recognition models](https://github.com/k2-fsa/icefall){:target="_blank"} and [deployment](https://github.com/k2-fsa/sherpa-onnx){:target="_blank"}, but also releases a large number of pre-trained models and corresponding demo programs.

## Huggingface space

The most direct and convenient way to experience the Next-gen Kaldi is to visit our provided Huggingface space with a browser, which currently supports the experience of dozens of models in languages such as Chinese, English, Chinese-English, Chinese-English-Cantonese, Cantonese, Tibetan, Arabic, German, French, and Russian.


[Huggingface :hugging: Space](https://huggingface.co/spaces/k2-fsa/automatic-speech-recognition){:target="_blank"}。

[![](../assets/images/asr_huggingface_en.png "Next-gen Kaldi speech recognition space")](https://huggingface.co/spaces/k2-fsa/automatic-speech-recognition){:target="_blank"}


### Webassembly

The Next-gen Kaldi also offers [webassembly](https://webassembly.org/){:target="_blank"} support, which allows you run the models totally in the browser and no server is needed. Here are several pre-compiled models in the following table. If you want to package your own models using webassembly, plsease refer to [sherpa-onnx docs](https://k2-fsa.github.io/sherpa/onnx/wasm/index.html){:target="_blank"} and [sherpa-ncnn docs](https://k2-fsa.github.io/sherpa/ncnn/wasm/index.html){:target="_blank"}

| Language                      | Encoder    | Inference Engine                                                          | Address                                                                                                                       | Model link                                                                                                                                                                                                                                        |
| ----------------------------- | ---------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| English                       | zipformer  | [onnxruntime](https://github.com/microsoft/onnxruntime){:target="_blank"} | [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-onnx-en){:target="_blank"}                         | [Docs for the model](https://k2-fsa.github.io/sherpa/onnx/pretrained_models/online-transducer/zipformer-transducer-models.html#csukuangfj-sherpa-onnx-streaming-zipformer-en-2023-06-21-english){:target="_blank"}                                |
| Chinese & English             | zipformer  | [onnxruntime](https://github.com/microsoft/onnxruntime){:target="_blank"} | [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-onnx-zh-en){:target="_blank"}                      | [Docs for the model](https://k2-fsa.github.io/sherpa/onnx/pretrained_models/online-transducer/zipformer-transducer-models.html#csukuangfj-sherpa-onnx-streaming-zipformer-bilingual-zh-en-2023-02-20-bilingual-chinese-english){:target="_blank"} |
| Chinese & English             | paraformer | [onnxruntime](https://github.com/microsoft/onnxruntime){:target="_blank"} | [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-onnx-zh-en-paraformer){:target="_blank"}           | [Docs for the model](https://k2-fsa.github.io/sherpa/onnx/pretrained_models/online-paraformer/paraformer-models.html#csukuangfj-sherpa-onnx-streaming-paraformer-bilingual-zh-en-chinese-english){:target="_blank"}                               |
| Chinese & English & Cantonese | paraformer | [onnxruntime](https://github.com/microsoft/onnxruntime){:target="_blank"} | [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-onnx-zh-cantonese-en-paraformer){:target="_blank"} | [Docs for the model](https://k2-fsa.github.io/sherpa/onnx/pretrained_models/online-paraformer/paraformer-models.html#csukuangfj-sherpa-onnx-streaming-paraformer-trilingual-zh-cantonese-en-chinese-cantonese-english){:target="_blank"}          |
| English                       | zipformer  | [ncnn](https://github.com/tencent/ncnn){:target="_blank"}                 | [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-ncnn-en){:target="_blank"}                         | [Docs for the model](https://k2-fsa.github.io/sherpa/ncnn/pretrained_models/zipformer-transucer-models.html#csukuangfj-sherpa-ncnn-streaming-zipformer-en-2023-02-13-english){:target="_blank"}                                                   |
| Chinese & English             | zipformer  | [ncnn](https://github.com/tencent/ncnn){:target="_blank"}                 | [huggingface](https://huggingface.co/spaces/k2-fsa/web-assembly-asr-sherpa-ncnn-zh-en){:target="_blank"}                      | [Docs for the model](https://k2-fsa.github.io/sherpa/ncnn/pretrained_models/zipformer-transucer-models.html#csukuangfj-sherpa-ncnn-streaming-zipformer-bilingual-zh-en-2023-02-13-bilingual-chinese-english){:target="_blank"}                    |


### Subtitle extraction

The subtitle extraction is a small tool we made based on speech recognition. Users can upload a video to generate the corresponding subtitle file. Huggingface space (support Chinese, English, Chinese-English, and Russian) [address :hugging:](https://huggingface.co/spaces/k2-fsa/generate-subtitles-for-videos){:target="_blank"}.


## Videos

> Note: All videos are in Chinese!

In order to make it easier for you to see the demo quickly, we have also made a lot of videos, see [:fontawesome-brands-bilibili: Bilibili](https://space.bilibili.com/1234519871/video?tid=0&special_type=&pn=1&keyword=&order=click){:target="_blank"} for details.


## apk & exe

We also offer a number of compiled android APK and Windows executables.

| Language                                  | Engine                                                                    | Platform | Download link                                                                                          |
| ----------------------------------------- | ------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| Chinese                                   | [onnxruntime](https://github.com/microsoft/onnxruntime){:target="_blank"} | Android  | [Link](../resources.md?s=onnx.*(x86\|x86_64\|arm64-v8a\|armeabi-v7a)-zh.apk){:target="_blank"}         |
| English                                   | [onnxruntime](https://github.com/microsoft/onnxruntime){:target="_blank"} | Android  | [Link](../resources.md?s=onnx.*(x86\|x86_64\|arm64-v8a\|armeabi-v7a)-en.apk){:target="_blank"}         |
| English & Chinese                         | [onnxruntime](https://github.com/microsoft/onnxruntime){:target="_blank"} | Android  | [Link](../resources.md?s=onnx.*(x86\|x86_64\|arm64-v8a\|armeabi-v7a)-bilingual.*apk){:target="_blank"} |
| English & Chinese                         | [ncnn](https://github.com/tencent/ncnn){:target="_blank"}                 | Android  | [Link](../resources.md?s=ncnn.*(x86\|x86_64\|arm64-v8a\|armeabi-v7a)-bilingual.*apk){:target="_blank"} |
| All language(download models by yourself) | [onnxruntime](https://github.com/microsoft/onnxruntime){:target="_blank"} | Windows  | [Link](../resources.md?s=asr.*exe){:target="_blank"}                                                   |
| All language(download models by yourself) | [ncnn](https://github.com/tencent/ncnn){:target="_blank"}                 | Windows  | [Link](../resources.md?s=ncnn.*exe){:target="_blank"}                                                  |