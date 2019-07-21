---
title: 大数据处理平台Hadoop（一）
date: 2019-07-17 16:42:54
tags: hadoop
categories: bigdata
copyright: true
---
> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多机器学习干货   
> github：https://github.com/aimi-cn/AILearners 

本文参考地址：[[apachecn/AiLearning](https://github.com/apachecn/AiLearning)]

本文出现的所有代码，均可在github上下载，不妨来个Star把谢谢~：[Github代码地址](https://github.com/aimi-cn/AILearners)
## 简要介绍

作为本公众号的一个新的分支，计算机视觉这件小事一般记录的是深度学习和人工智能的学习笔记，今天将为大家献上大数据及大数据处理平台，分布式的一些笔记，以上是大数据平台关于hadoop的简介，以后将带领大家一步步走入大数据的学习，在学习前，我们应该先了解hadoop的简介，在接下来的一些章节，将为大家讲解hadoop的搭建安装，还有一些大数据工具，Hbase，Hive，Spark，zookeeper等等。

# 大数据处理平台Hadoop（一）

## Hadoop发展

Hadoop是Doug Cutting（Apache Lucene创始人）开发的使用广泛的文本搜索库。Hadoop起源于Apache Nutch，后者是一个开源的网络搜索引擎，本身也是由Lucene项目的一部分。<!--more-->

Hadoop这个名字不是一个缩写，它是一个虚构的名字。该项目的创建者，Doug Cutting如此解释Hadoop的得名："这个名字是我孩子给一头吃饱了的棕黄色大象命名的。我的命名标准就是简短，容易发音和拼写，没有太多的意义，并且不会被用于别处。小孩子是这方面的高手。Googol就是由小孩命名的。"  

Nutch项目开始于2002年，一个可工作的抓取工具和搜索系统很快浮出水面。但他们意识到，他们的架构将无法扩展到拥有数十亿网页的网络。在 2003年发表的一篇描述Google分布式文件系统(简称GFS)的论文为他们提供了及时的帮助，文中称Google正在使用此文件系统。GFS或类似的东西，可以解决他们在网络抓取和索引过程中产生的大量的文件的存储需求。具体而言，GFS会省掉管理所花的时间，如管理存储节点。在 2004年，他们开始写一个开放源码的应用，即Nutch的分布式文件系统(NDFS)。
2004年，Google发表了论文，向全世界介绍了MapReduce。2005年初，Nutch的开发者在Nutch上有了一个可工作的MapReduce应用，到当年年中，所有主要的Nutch算法被移植到使用MapReduce和NDFS来运行。

Nutch中的NDFS和MapReduce实现的应用远不只是搜索领域，在2006年2月，他们从Nutch转移出来成为一个独立的Lucene 子项目，称为Hadoop。大约在同一时间，Doug Cutting加入雅虎，Yahoo提供一个专门的团队和资源将Hadoop发展成一个可在网络上运行的系统。在2008年2月，雅虎宣布其搜索引擎产品部署在一个拥有1万个内核的Hadoop集群上。  

2008年1月，Hadoop已成为Apache顶级项目，证明它是成功的，是一个多样化、活跃的社区。通过这次机会，Hadoop成功地被雅虎之外的很多公司应用，如Last.fm、Facebook和《纽约时报》。

2008年4月，Hadoop打破世界纪录，成为最快排序1TB数据的系统。运行在一个910节点的群集，Hadoop在209秒内排序了1TB的数据，击败了前一年的297秒冠军。同年11月，谷歌在报告中声称，它的MapReduce实现执行1TB数据的排序只用了68 秒。 在2009年5月，有报道宣称Yahoo的团队使用Hadoop对1 TB的数据进行排序只花了62秒时间。

<img src="https://chen-tzliang.github.io/about/hadoopImages/hadoop发展图.png" width="100%" height="10%"/>

<center>
图1 hadoop发展图
</center>

十年前还没有Hadoop，几年前国内IT圈里还不知道什么是Hadoop，而现在几乎所有大型企业的IT系统中有已经有了Hadoop的集群在运行了各式各样的任务。

2006年项目成立的一开始，“Hadoop”这个单词只代表了两个组件——HDFS和MapReduce。到现在的10个年头，这个单词代表的是“核心”（即Core Hadoop项目）以及与之相关的一个不断成长的生态系统。这个和Linux非常类似，都是由一个核心和一个生态系统组成。
现在Hadoop俨然已经成为企业数据平台的“新常态”。我们很荣幸能够见证Hadoop十年从无到有，再到称王。

## Hadoop的体系结构

Hadoop是一个能够对大量数据进行分布式处理的软件框架。具有可靠、高效、可伸缩的特点。Hadoop的核心是HDFS（分布式文件系统）和MapReduce（分布式运算编程框架），Hadoop2.0还包括YARN（运算资源调度系统）。

整个Hadoop的体系结构主要是通过HDFS来实现对分布式存储的底层支持，并通过MR来实现对分布式并行任务处理的程序支持。

本节在具体介绍Hadoop体系结构之前，先用一个流程图介绍Hadoop业务的开发流程。
<img src="https://chen-tzliang.github.io/about/hadoopImages/hadoop业务开发流程图.png" width="100%" height="10%"/>
<center>
图2 hadoop业务开发流程图
</center>

<img src="https://chen-tzliang.github.io/about/hadoopImages/hadoop的核心组件图.png" width="100%" height="10%"/>
<center>
图3 hadoop的核心组件图
</center>

**Hadoop Common**

Hadoop Common 为Hadoop 整体架构提供基础支撑性功能，主要包括了文件系统（File System）、远程过程调用协议（RPC）和数据串行化库（Serialization Libraries）。

**Hadoop Distributed File System(HDFS)**

HDFS是一个适合构建廉价计算机集群之上的分布式文件系统，具有低成本、高可靠性、高吞吐量的特点，由早期的NDFS演化而来。

**MapReduce**

MapReduce是一个编程模型和软件框架，用于在大规模计算机集群上编写对大数据进行快速处理的并行化程序。

**HBase**

HBase是一个分布式的、面向列的开源数据库，不同于一般的关系数据库，它是一个适合于非结构化大数据存储的数据库。

**HCatalog**

HCatalog是一个用于管理hadoop产生数据的表存储管理系统。它提供了一个共享的数据模版和数据类型的机制，并对数据表进行抽象以方便用户仅需要关注数据结构设计而不需要考虑数据是如何存储的，同时支持hadoop不同数据处理工具之间的互联互通。

**Hive**

Hive是一个基于hadoop的数据仓库工具，它可以将结构化的数据文件映射为一张数据库表，并提供强大的类SQL查询功能，可以将SQL语句转换为MapReduce任务进行运行。

**Pig**

Pig是一个用于大数据分析的工具，包括了一个数据分析语言和其运行环境。Pig的特点是其结构设计支持真正的并行化处理，因此适合应用于大数据处理环境。

**Sqoop**

Sqoop是一款用于hadoop系统与传统数据库间进行数据交换的工具，可以用于传统数据库（如MYSQL、Oracle）中数据导入HDFS或MapReduce，并将处理后的结果导出到传统数据库中。

**Avro**

Avro是一个基于二进制数据传输高性能中间件，可以做到将数据进行序列化，适用于远程或本地大批量数据交互。

**Chukwa**

Chukwa是一个分布式数据收集和分析系统，用于监控大型分布式系统。Chukwa基于HDFS和MapReduce构建而成，并提供了一系列工具用于显示、监控、分析系统运行数据。

**Ambari**

Ambari是一个用于安装、管理、监控hadoop集群的web界面工具。目前已支持包括MapReduce、HDFS、HBase在内的几乎所有hadoop组件的管理。

**ZooKeeper**

ZooKeeper是一个分布式应用程序协调服务器，用于维护hadoop集群的配置信息、命名信息等，并提供分布式锁同步功能和群组管理功能。

## Hadoop的特点

**（1）支持超大文件**

一般来说，HDFS存储的文件可以支持TB和PB级别的数据。

**（2）检测和快速应对硬件故障**

在集群环境中，硬件故障是常见性问题。因为有上千台服务器连在一起，故障率高，因此故障检测和自动恢复是HDFS文件系统的一个设计目标。假设某一个DataNode节点挂掉之后，因为数据备份，还可以从其他节点里找到。NameNode通过心跳机制来检测DataNode是否还存在。

**（3）流式数据访问**

HDFS的数据处理规模比较大，应用一次需要大量的数据，同时这些应用一般都是批量处理，而不是用户交互式处理，应用程序能以流的形式访问数据库。主要的是数据的吞吐量，而不是访问速度。访问速度最终是要受制于网络和磁盘的速度，机器节点再多，也不能突破物理的局限，HDFS不适合于低延迟的数据访问，HDFS的是高吞吐量。 

**（4）简化的一致性模型**

对于外部使用用户，不需要了解Hadoop底层细节，比如文件的切块，文件的存储，节点的管理等。 
一个文件存储在HDFS上后，适合一次写入、多次写出的场景once-write-read-many。因为存储在HDFS上的文件都是超大文件，当上传完这个文件到Hadoop集群后，会进行文件切块、分发、复制等操作。如果文件被修改，会导致重新执行这个过程，而这个过程耗时是最长的。所以在Hadoop里，不允许对上传到HDFS上文件做修改（随机写），在2.0版本可以在后面追加数据。但不建议。 

**（5）高容错性**

数据自动保存多个副本，副本丢失后自动恢复。可构建在廉价机上，实现线性（横向）扩展，当集群增加新节点之后，NameNode也可以感知，将数据分发和备份到相应的节点上。

**（6）商用硬件**

Hadoop并不需要运行在昂贵且高可靠的硬件上，它是设计运行在商用硬件的集群上的，因此至少对于庞大的集群来说，节点故障的几率还是非常高的。HDFS遇到上述故障时，被设计成能够继续运行且不让用户察觉到明显的中断。


