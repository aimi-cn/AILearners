# 【2019斯坦福CS224N笔记】（12）Information from parts of words: Subword Models

csdn：https://blog.csdn.net/abcgkj

github：https://github.com/aimi-cn/AILearners

---

## 基于word level的模型

在我们使用基于word level的模型时，需要处理很大的词汇表，而且在英语中单词只要变个形态就是另一个单词了，比如对于下图的一些非正式表达：因此会遇到很大的麻烦。

![](../../../img/nlp/cs224n/12Information&#32;from&#32;parts&#32;of&#32;words&#32;Subword&#32;Models/TIM截图20190806212924.png)

## 基于character level的模型

而采用基于character level的模型，可以为未知单词生成word embedding ，相似的拼写单词会有相似的word embedding，并且可以解决OOV问题。

对于纯字符级的模型来说，开始时并没有得到令人满意的效果。但是在2015年之后，逐渐由研究者取得了一些成绩。比如说，luong和Manining测试了一个纯字符级的seq2seq（LSTM）NMT系统作为baseline，它和基于word level的模型一样运行的很好，但是在训练时非常耗费时间。下图来是该系统的BLEU评分：

![](../../../img/nlp/cs224n/12Information&#32;from&#32;parts&#32;of&#32;words&#32;Subword&#32;Models/TIM截图20190806214309.png)

下图是使用该系统翻译的一个例子,可以看到字符级的模型有很好的效果：

![](../../../img/nlp/cs224n/12Information&#32;from&#32;parts&#32;of&#32;words&#32;Subword&#32;Models/TIM截图20190806214427.png)

在2017年，Jason Lee等人开发出一种Fully Character-Level Neural Machine Translation without Explicit Segmentation系统，下图是该模型的Encoder，Decoder是一个char-level的GRU。

![](../../../img/nlp/cs224n/12Information&#32;from&#32;parts&#32;of&#32;words&#32;Subword&#32;Models/TIM截图20190806214635.png)

2018年Google的一些研究人员对基于LSTM的seq2seq的character level模型进行分析发现，模型深度越深得到的效果越好，而且char level系统比word level系统表现好，但是char level系统所花费的时间却比word level系统长的多，如下图所示：

![](../../../img/nlp/cs224n/12Information&#32;from&#32;parts&#32;of&#32;words&#32;Subword&#32;Models/TIM截图20190806215259.png)

## Sub-word模型的两个趋势

- 与word level相同的架构，但是使用更小的单元：“word pieces”
- 混合架构：主要为word级，也有一部分为character

对于第一种，Google NMT使用了贪婪贪婪近似最大化语言模型的似然函数来选择pieces，该模型标记内部单词，空格保留为特殊标记(_)并正常分组。

而对于第二种，2014年Dos Santos和Zadrozny提出了Character-level to build word-level Learning Character-level Representations for Part-of-Speech Tagging，该模型对字符进行卷积以生成单词嵌入，并且在固定窗口的词嵌入中使用PoS标签，如下图所示：

![](../../../img/nlp/cs224n/12Information&#32;from&#32;parts&#32;of&#32;words&#32;Subword&#32;Models/TIM截图20190806220450.png)

Ling等人提出了Character-based LSTM  to build word rep’ns，即使用双向LSTM来构建word representations，

为了构建出一个强大、健壮的语言模型，且该模型在多种语言中都有效，编码子单词关联性和用更少的参数获得可比较的表达性，研究人员提出了下图所示的架构：

![](../../../img/nlp/cs224n/12Information&#32;from&#32;parts&#32;of&#32;words&#32;Subword&#32;Models/TIM截图20190806220914.png)

在2016年，Bojanowski等人提出了FastText embeddings，其目的是推出一种更高效的类似word2vecd的单词表示库，并且更适合于具有大量形态学的稀有单词和语言，对于一个单词的表示采用n-grams和其整个单词来共同表示，如下图所示:

![](../../../img/nlp/cs224n/12Information&#32;from&#32;parts&#32;of&#32;words&#32;Subword&#32;Models/TIM截图20190806221908.png)

喜欢的童鞋记得分享给别的小伙伴哈。AIMI-CN AI学习交流群【1015286623】 获取更多AI资料扫码加群：

<div align=center><img src="../../../img/otherImages/gkj/QRcode_qq.png" /></div>

分享技术，乐享生活：我们的公众号每周推送“AI”系列资讯类文章，欢迎您的关注！

<div align=center><img src="../../../img/otherImages/gkj/QRcode_wechart.png" /></div>