

## CS224n-01课程简介和词向量

- 课程介绍
- 人类语言和词义
- word2vec介绍
- word2vec目标函数梯度
- 优化基础
- word vectors

### 一、课程介绍

1. [课程官网](http://cs224n.stanford.edu/)
2. 2019版课程与之前课程的区别：环境为Pytorch，且内容更为紧凑

### 二、人类语言和词义

#### 1.我们如何在计算机中拥有可用的意思？

一般的解决方案：使用WordNet（一个包含同义词集和超常词列表的同义词典）。

*举例：包含“good”的同义词集合*

**代码示例**

```python
import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')
poses = { 'n':'noun', 'v':'verb', 's':'adj (s)', 'a':'adj', 'r':'adv'}
for synset in wn.synsets("good"):
    print("{}: {}".format(poses[synset.pos()], ", ".join([l.name() for l in 			synset.lemmas()])))
```

**output**

	noun: good
	noun: good, goodness
	noun: good, goodness
	noun: commodity, trade_good, good
	adj: good
	adj (s): full, good
	adj: good
	adj (s): estimable, good, honorable, respectable
	adj (s): beneficial, good
	adj (s): good
	……
	adv: well, good
	adv: thoroughly, soundly, good

#### 2.诸如WordNet的资源中存在的问题

- 作为一个资源很好，但缺少细微差别

  例如：“proficient”被列为“good”的同义词。但是这仅仅在某些语境下是成立的。

- 缺少单词的新含义

  例如：wicked, badass, nifty, wizard, genius, ninja, bombest

  不能与时俱进

- 主观性

- 需要人为来创造和适应

- 无法计算准确的单词相似性

#### 3.用离散符号来表示单词

在传统的自然语言处理中，我们把词语看作离散的符号:hotel, conference, motel – a localist representation

![1556277878961](C:\Users\gkj\AppData\Roaming\Typora\typora-user-images\1556277878961.png)

向量维数=词汇表中单词的数量(如500,000)

#### 4.把单词当作离散符号的问题

例如：在web搜索中，如果用户搜索“Seattle motel”,我们希望匹配包含“Seattle hotel”。

但是，

![1556278099742](C:\Users\gkj\AppData\Roaming\Typora\typora-user-images\1556278099742.png)

这两个向量是**正交**的。对于one-hot向量，没有**相似性**概念!

#### 5.解决方案

我们可以学习在向量本身中编码相似性，即**根据上下文来表示单词**。

​	*Distributional semantics*: **A word’s meaning is given by the words that frequently appear close-by**

- “You shall know a word by the company it keeps” (J. R. Firth 1957: 11)
- **One of the most successful ideas of modern statistical NLP!**	

当一个单词w出现在文本中时，它的**context**是出现在附近的一组单词(在一个**固定大小**的窗口中)。

使用w的许多contexts来构建w的表示

![1556278562922](C:\Users\gkj\AppData\Roaming\Typora\typora-user-images\1556278562922.png)

### 三、词向量（word2vec）介绍

#### 1.word vectors

- 我们将为选择的每个单词构建一个密集的向量，使其类似于出现在类似上下文中的单词的向量。

  *注：word vectors有时被称为word embeddings或word representations表示。它们是一种分布式的表示。*

- 词的含义作为一个神经词向量——可视化

![1556279078631](C:\Users\gkj\AppData\Roaming\Typora\typora-user-images\1556279078631.png)

#### 2.word2vec回顾

**如对word2vec还有疑问，请看**[图文讲解word2vec](https://blog.csdn.net/abcgkj/article/details/89575872)

Word2vec (Mikolov et al. 2013)是一个学习单词向量的框架

**主要思想：**

- 我们有大量的文本语料库
- 固定词汇表中的每个单词都由一个**向量**表示
- 遍历文本中的每个位置t，其中有一个中心词(center)c和上下文词(“outside”)单词o
- 用向量c和o的**相似度**（比如说余弦相似度）来计算给定c的o的**概率**(**反之亦然**)，即Word2vec是一种从原始文本中学习嵌入词的高效预测模型。它有两种风格:连续的词袋模型(CBOW)和**跳格模型(skip-gram)**。从算法上来说，这些模型是相似的，CBOW从源上下文词预测目标词，而skip-gram则相反，**从目标词预测源上下文词**。)
- 不断调整单词向量来**最大化**这个概率

**示例（给定windows来计算P(w_{t+j}|w_t)：**



![1556281464315](1556281464315.png)



#### 3.word2vec：objective function

对于每个位置t= 1，…，T，预测一个固定大小为m的窗口、中心词为w_j，预测context words：

![1556281972715](C:\Users\gkj\AppData\Roaming\Typora\typora-user-images\1556281972715.png)

**注：**

- objective function，有时也被称作loss function或者cost function
- θ是所有要被优化的变量
- 目标函数相比于上面的似然函数，前面加了一个负号，由最大值改为求最小值，这点并没有很大区别

**因此，我们想要得到目标函数的最小值**:
$$
J(θ)=-\frac{1}{T}\sum^T_{t=1}\sum_{\substack{-m\le j\le m \\j\neq0}}logP(w_{t+j}|w_t;\theta)
$$

- 问题：如何计算P？
- 答案：对于每个单词w，我们将使用两个向量：
  - v_w，当w是中心词的时候
  - u_w，当w是上下文词的时候
- 此时，对于中心词c和上下文词o:

$$
P(o|c)=\frac{exp(u _o^Tv_c)}{\sum_{w\in V}exp(u _w^Tv_c)}
$$

![1556284884279](C:\Users\gkj\AppData\Roaming\Typora\typora-user-images\1556284884279.png)

#### 4.softmax function

这是一个[softmax function](https://zh.wikipedia.org/wiki/Softmax%E5%87%BD%E6%95%B0)(归一化处理)的例子：
$$
softmax(x_i)=\frac{exp(x_i)}{\sum_{j=1}^nexp(x_j)}=p_i
$$
softmax function将任意值x_i映射到概率分布p_i上

- Exponentiation makes anything positive

- “max” because amplifies probability of largest x_i
- “soft” because still assigns some probability to smaller x_i
- Frequently used in Deep Learning

### 四、通过优化参数来训练模型

为了训练模型，我们调整参数使损失最小化。例如，对于两个参数上的一个简单凸函数，等高线表示目标函数的级别

![1556285603734](C:\Users\gkj\AppData\Roaming\Typora\typora-user-images\1556285603734.png)

#### 1.训练模型:计算**所有**向量梯度

- 回忆:θ表示在一个长向量中所有模型参数
- 

