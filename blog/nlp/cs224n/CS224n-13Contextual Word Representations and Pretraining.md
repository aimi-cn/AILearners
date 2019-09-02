# 【2019斯坦福CS224N笔记】（13）Contextual Word Representations and Pretraining

csdn：https://blog.csdn.net/abcgkj

github：https://github.com/aimi-cn/AILearners

---

## 词向量的表示

目前为止，我们已经学过了one-hot编码、word2vec、glove等词向量的表示。但是这三个方法都普遍存在在一些问题，就是无法解决一词多义的问题。即对于同一个词无论上下文的单词是否相同，训练出来的词向量都是一样的。

当我们手中的语料不足时训练出来的词向量效果不会很理想，这时我们可以使用他人已经训练好的词向量，并且以预训练的词向量来作为初始值，在训练过程中进行微调。下图是2011年Collobert, Weston等人使用预训练的词向量进行NLP任务的精度和F1值，模型使用了预训练词向量之后，得分得到了提升：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190813212133.png)

但是，我们训练好的词向量是不可能涵盖所有词的(这里主要有两个原因，一是训练语料中本来就不存在这些词，二是这些词在训练语料中出现次数过少)，这就会存在一个未登录词（unknown words）的问题，遇到这个问题的时候我们怎么处理呢？常见的解决方案是：

- 首先，最简单和最普遍的解决方法就是将所有未登录的词映射为<UNK>，并且为它训练一个词向量。但是这种方法存在缺点，它把这些未登录词都视为相同，不能区分它们的区别。
- 训练字符级的词向量
- 此外，你可以将其视为新的单词，并为其分配一个随机向量，将它们添加到你的词汇表。

不过，对于这样的解决方案存在着一定的问题，即：我们没有办法区分不同的unknown words。此外，到目前为止，对于每一个单词，我们都只拥有一个词向量，因此很难解决一词多义的问题。接下来，我们介绍一些经典模型。

## 经典模型

### 1.Peters et al. (2017): TagLM – “Pre-ELMo”

核心思想：通过上下文中获取单词的含义，但只在task-labeled的任务（例如，NER）上使用RNN来进行训练。算法的核心步骤如下：

- 在未标记的数据上预训练词向量和语言模型
- 在输入序列中准备好单词嵌入和语言模型嵌入。
- 在序列标记模型中同时使用单词嵌入和语言模型嵌入。

模型结构图如下：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902170258.png)

论文得出的结论如下：

- 通过对语言模型观察我们得出：使用有监督数据集来训练的语言模型效果甚微，使用双向语言模型仅对向前有利，网络结构越复杂效果越好。
- 通过对任务特定BILSTM观察可知：仅使用lm嵌入来预测并不好

## 2.Peters et al. (2018): ELMo: Embeddings from Language Models

在下一年，Peters等人提出的ELMo模型在非常多的NLP task上都提高了state-of-the-art 方法的performance, 被一些人称为新的word2vec. 这文章同时被ICLR 2018 和NAACL 2018 接收, 后来获得了NAACL best paper award。

ELMO是第一个使用双向语言模型来获得词向量的方法。这里使用长上下文而不是上下文窗口学习单词标记向量，使用双向的深层NLM进行训练并使用其所有层进行预测。

我们来简要介绍下这个模型：首先，它训练了一个双向的语言模型，其次，其性能很好并且模型不大：使用2个bilstm层，使用字符级的CNN建立初始单词表示(2048 char n-gram过滤器和2个HighWay层，512 dim投影)，使用4096 dim hidden/cell lstm状态，512dim投影到下一个输入，使用残差网络连接token输入和输出（SoftMax）的参数，并将这些参数连接在正向和反向语言模型之间。

ELMO用于学习特定任务的双向语言模型表示的组合，这是首次仅使用LSTM堆栈顶层的模型，ELMO的任务可以简单表示为：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902174116.png)

在使用双向语言模型获得词向量后，我们在下游任务中使用词向量时，冻结有监督模型中的ELMO部分，并且将EMLO的权重根据不同的任务来连接不同的模型中。模型中的两个bilstm nlm层具有不同的用途/含义:较低层学习的是较低级别的语法等,比如词性标注，句法依赖，NER等任务；高层次学习的是语义，可用于情感，语义角色标注，问题回答等任务。

## 3.ULMfit

Howard and Ruder (2018)提出了 Universal Language Model Fine-tuning for Text Classification。ULMfit主要是使用迁移学习来进行文本分类。迁移学习示意图如下：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902175053.png)

该模型的核心思想是：

- 在大的通用域语料库上训练神经语言模型
- 在目标任务数据上微调语言模型
- 采用该模型，将其从语言模型转化
- 为分类器

模型结构图如下：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902175657.png)

该模型在训练时有一些细节：

- 每层使用不同的学习率，即Slanted triangular learning rate (STLR) schedule，开始学习率逐渐增大，后面逐渐变小
- 在学习分类器时逐步解冻并且采用STLR策略
- 分类时使用下图拼接的方法：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902180041.png)

## 4.Transformer

transformer的出现主要是为了利用纯attention来解决RNN系列网络无法并行计算的问题。模型结构图如下所示：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/v2-4b53b731a961ee467928619d14a5fd44_hd.jpg)

我们从图中可以看到：和大多数seq2seq模型一样，transformer的结构也是由encoder和decoder组成。最初应用于使用并行语料库进行机器翻译并预测每个单词的翻译。

### 1.Encoder

Encoder由N=6个相同的layer组成，layer指的就是上图左侧的单元，最左边有个“Nx”，这里是x6个。每个Layer由两个sub-layer组成，分别是multi-head self-attention mechanism和fully connected feed-forward network。其中每个sub-layer都加了residual connection和normalisation，因此可以将sub-layer的输出表示为：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902182117.png)

首先我们先看一下Multi-head self-attention。对于普通的attention机制，可以用以下形式表示：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902182614.png)

multi-head attention则是通过h个不同的线性变换对Q，K，V进行投影，最后将不同的attention结果拼接起来并通过线性层传输，，可以用以下公式表达：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902182805.png)

与CNN和传统的Attention相比，Multi-head attention还是有很多特性的。下面以这句话为例子：The cat stuck out its tongue and licked its owner。当使用CNN处理这段话时，体现的是相对位置的不同线性变换。

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902184300.png)

当使用普通的Attention时，体现的是权重的平均,如下图所示：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902184328.png)

当使用Multi-Attention时，在输入和输出上具有不同线性变换的并行行Attention层,如下图所示：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902184355.png)

其次是Position-wise feed-forward networks。这层主要是提供非线性变换。

### 2.Decoder

Decoder和Encoder的结构差不多，但是多了一个attention的sub-layer，这里先明确一下decoder的输入输出和解码过程：

- 输入：encoder的输出和对应i-1位置decoder的输出。所以中间的attention不是self-attention，它的K，V来自encoder，Q来自上一位置decoder的输出
- 输出：对应i位置的输出词的概率分布
- 解码：这里要特别注意一下，编码可以并行计算，一次性全部encoding出来，但解码不是一次把所有序列解出来的，而是像rnn一样一个一个解出来的，因为要用上一个位置的输入当作attention的query

明确了解码过程之后最上面的图就很好懂了，这里主要的不同就是新加的另外要说一下新加的attention多加了一个mask，因为训练时的output都是ground truth，这样可以确保预测第i个位置时不会接触到未来的信息。

### 3.Positional Encoding

截止目前为止，我们介绍的Transformer模型并没有捕捉顺序序列的能力，也就是说无论句子的结构怎么打乱，Transformer都会得到类似的结果。换句话说，Transformer只是一个功能更强大的词袋模型而已。

为了解决这个问题，论文中在编码词向量时引入了位置编码（Position Embedding）的特征。具体地说，位置编码会在词向量中加入了单词的位置信息，这样Transformer就能区分不同位置的单词了。那么怎么编码这个位置信息呢？常见的模式有：a. 根据数据学习；b. 自己设计编码规则。在这里作者采用了第二种方式。那么这个位置编码该是什么样子呢？通常位置编码是一个特征向量，这样便于和词向量进行单位加的操作。论文给出的编码公式如下：

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/TIM截图20190902184904.png)

在上式中,pos表示单词的位置，i表示单词的维度。关于位置编码的实现可在Google开源的算法中[get_timing_signal_1d()](https://github.com/tensorflow/tensor2tensor/blob/23bd23b9830059fbc349381b70d9429b5c40a139/tensor2tensor/layers/common_attention.py)函数找到对应的代码。

作者这么设计的原因是考虑到在NLP任务重，除了单词的绝对位置，单词的相对位置也非常重要。根据公式sin(α+β)=sinαcosβ+cosαsinβ以及cos(α+β)=cosαcosβ-sinαsinβ，这表明位置k+p的位置向量可以表示为位置k的特征向量的线性变化，这为模型捕捉单词之间的相对位置关系提供了非常大的便利。

Transformer是第一个用纯attention搭建的模型，算法的并行性非常好，并且在翻译任务上也获得了更好的结果，因此Transformer也可以用在NLP的其他任务上。但是，Transformer一味的去除掉了RNN，因此RNN和Transformer的结合也许会更好。

## 5.BERT

Bert模型是Google在2018年10月发布的语言表示模型，Bert在NLP领域横扫了11项任务的最优结果，可以说是最近NLP中最重要的突破。Bert模型的全称是Bidirectional Encoder Representations from Transformers，BERT模型的目标是利用大规模无标注语料训练、获得文本的包含丰富语义信息的Representation，即：文本的语义表示，然后将文本的语义表示在特定NLP任务中作微调，最终应用于该NLP任务。

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/微信截图_20190902211956.png)

BERT模型的主要输入是文本中各个字/词的原始词向量，该向量既可以随机初始化，也可以利用Word2Vector等算法进行预训练以作为初始值；输出是文本中各个字/词融合了全文语义信息后的向量表示。

BERT将多个transformer编码器堆叠在一起。BERT卓越的性能基于两点。首先创新预训练任务Masked Language Model (MLM)以及Next Sentence Prediction (NSP). 其次训练BERT使用了大量数据和算力。

MLM使得BERT能够从文本中进行双向学习，也就是说这种方式允许模型从单词的前后单词中学习其上下文关系。此前的模型这是做不到的。此前最优的算法称为Generative Pre-training (GPT) 该方法采用了从左到右的训练方式，另外ELMo 采用浅双向学习(shallow bidirectionality)。

![](../../../img/nlp/cs224n/13Contextual&#32;Word&#32;Representations&#32;and&#32;Pretraining/微信截图_20190902210936.png)

而近日，百度提出知识增强的语义表示模型 ERNIE（Enhanced Representation from kNowledge IntEgration），并发布了基于 PaddlePaddle 的开源代码与模型，在语言推断、语义相似度、命名实体识别、情感分析、问答匹配等自然语言处理（NLP）各类中文任务上的验证显示，模型效果全面超越 BERT。由此可以看出，预训练模型已成为近来NLP领域的潮流。

喜欢的童鞋记得分享给别的小伙伴哈。AIMI-CN AI学习交流群【1015286623】 获取更多AI资料扫码加群：

<div align=center><img src="../../../img/otherImages/gkj/QRcode_qq.png" /></div>

分享技术，乐享生活：我们的公众号每周推送“AI”系列资讯类文章，欢迎您的关注！

<div align=center><img src="../../../img/otherImages/gkj/QRcode_wechart.png" /></div>