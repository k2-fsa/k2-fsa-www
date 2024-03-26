---
comments: true
title: 新一代 Kaldi 历程
---

## 2024 年

### 3月

#### icefall

- 增加使用 [LoRA](https://arxiv.org/abs/2106.09685){:target="_blank"} 微调的 recipe，[代码](https://github.com/k2-fsa/icefall/pull/1540){:target="_blank"}。
- 增加使用 [adapter](https://arxiv.org/pdf/1902.00751.pdf){:target="_blank"} 微调的 recipe，[代码](https://github.com/k2-fsa/icefall/pull/1512){:target="_blank"}, [文档](https://k2-fsa.github.io/icefall/recipes/Finetune/adapter/finetune_adapter.html){:target="_blank"}。
- 增加使用预训练 zipformer 做微调的 recipe，[代码](https://github.com/k2-fsa/icefall/pull/1484){:target="_blank"}, [文档](https://k2-fsa.github.io/icefall/recipes/Finetune/from_supervised/finetune_zipformer.html){:target="_blank"}。


#### sherpa

- 增加 webassembly 支持
- 增加 kws 支持


### 2月