---
title: 新一代 Kaldi 主页发布
date: 2024-04-01
categories:
  - Document
comments: true
authors:
  - pkufool
slug: homepage
---

与 Kaldi 是个单一项目不同，新一代 Kaldi 是一个项目集合，整个大项目中分成了很多负责不同子功能的小项目，各个小项目都相对独立且有自己的文档系统，这就给开发者带来了一些麻烦，很多开发者经常困惑各个子项目之间是什么关系？ 他们如何分工？ 该怎么最快找到自己需要的文档？ 为此，我们开发了一个简单的大项目主页，这个主页不是为了替代各子项目的文档，而是希望它成为整个大项目的总入口，方便大家最快找到自己需要的东西。

<!-- more -->

整个主页主要包含以下几个部分，下面做稍微详细的介绍。

## 首页

首页目前主要是罗列了新一代 Kaldi 目前发布的主要项目和对应简介。~~拉到下面看，上面部分看字就行，搞成这样纯粹为了好看~~

[![](../../assets/images/homepage/main.jpg)](../../index.md)

## 快速开始

快速开始页是各个项目和任务的开始指引，我们希望用户可以从这里快速找到开始一个项目/任务的路径和文档。每个项目的简单介绍和安装方法也会放在此处。

[![](../../assets/images/homepage/get_started.jpg)](../../get-started/index.md)

## 模型

模型页会有我们发布的一系列预训练模型，开发者们最常问的问题就是我该用哪个模型，我们希望这个页面能够回答大多数这样的问题。

[![](../../assets/images/homepage/model.jpg)](../../models/asr.md)

## 演示

演示也是大家常说的 Demo， 这个页面会列出各个任务我们精心制作的 Demo，包括但不限于视频、APK、exe、huggingface space 等等。

[![](../../assets/images/homepage/demo.jpg)](../../demos/asr.md)

## 重要事件

新一代 Kaldi 项目众多，有些开发者可能没有订阅 github，就算订阅了，消息太多估计也看不过来，所以这个页面，我们会列出项目的一些重要更新和发布的一些新特性。

[![](../../assets/images/homepage/event.jpg)](../../events.md)

## 论文

这个最好理解，就是团队发表的论文列表。

[![](../../assets/images/homepage/papers.jpg)](../../publications.md)

## 资源文件

资源文件页是给用户提供的一个快捷搜索入口，新一代 Kaldi 有很多项目，每个项目都会发布预训练模型，Demo 等等，这个页面将几乎左右的资源都汇总了，用户可以在页面上通过搜索的方式快速获得对应的链接，目前支持常规的字符串搜索和简单的正则支持。

[![](../../assets/images/homepage/resources.jpg)](../../resources.md)

## 博客

博客栏目是我们不定期发布的一些技术解读和各种希望与开发者分享的材料，后面我们也会把微信公众号的文章在这里同步发表。

[![](../../assets/images/homepage/blog.jpg)](../../blog/index.md)

## 留言板

其实我们各个页面下面都有对应的评论，项目的评论系统是基于 github 的，选择 github 也是为了便于管理，但考虑到中国大陆有些同学登 github 比较痛苦，所以中文的留言板我们给大家留了一个后门，可以不用登录即可留言，当然，我们不建议大家使用这个留言板，有条件还是使用 github 的评论系统，这样管理和追踪评论都比较方便。
[![](../../assets/images/homepage/message.jpg)](../../message.md)