# Feature selection

## ANOVA（方差分析）

#### 原理：

用于两个及两个以上样本均数差别的显著性检验。


$$
F(\xi)=\dfrac{s_{B}^{2}(\xi)}{s_{W}^{2}(\xi)}
$$

$$
s_B^2(\xi)=\sum_{i=1}^{K}m_i\frac{\left ( \frac{\sum_{j=1}^{m_i}f_{\xi}^g(i,j)}{m_i}-\frac{\sum_{i=1}^{K}\sum_{j=1}^{m_i}f_{\xi}^g(i,j)}{\sum_{i=1}^{K}m_i} \right )^2}{df_B}
$$

$$
s_W^2(\xi)=\sum_{i=1}^{K}\sum_{j=1}^{m_i}\frac{\left ( f_{\xi}^g(i,j)-\frac{\sum_{j=1}^{m_i}f_{\xi}^g(i,j)}{m_i} \right )^2}{df_W}
$$

F值就是组间差距和组内差距的比值，这个F值越大意味着某个特征具有更好的区分正负样本的能力。因此，所有的特征都可以根据这个F值进行排序。

#### 用法：

- ***ANOVA.py*** 

**程序说明：** 

使用方差分析思想对输入特征进行共线性大小排序（支持多分类）

**参数说明：** 

-i 输入文件，csv格式文件 
-o 输出文件，特征排序后的结果文件 

**用法实例：**

```
python ANOVA.py -i test.csv -o result.anova
```

**算法参考** 

`[1] Lin, H. et al. Predicting cancerlectins by the optimal g-gap dipeptides. Scientific reports 5, doi:10.1038/srep16964 (2015)` 



## F-Score

#### 原理：

F-Score 是度量特征在不同类别间的区分度的一种指标， F-Score值越大， 代表该特征在不同类别之间的区分度越强 . 假设 xk 代表数据集中的样本（k = 1,2,…,N） . n+为正类样本的数量， n-为负类样本的数量， 则数据集中第i个特征的F-Score可由


$$
F_i=\frac{(\bar{x}_i^{(+)}-\bar{x}_i)^2+(\bar{x}_i^{(-)}-\bar{x}_i)^2}{\frac{1}{n_+-1}\sum_{k=1}^{n_+}(x_{k,i}^{(+)}+\bar{x}_i^{(+)})^2+\frac{1}{n_{-}-1}\sum_{k=1}^{n_{-}}(x_{k,i}^{(-)}-\bar{x}_i^{(-)})^2}
$$

#### 用法：

- ***Fscore.py*** 

**程序说明：** 

使用Fscore的原理对输入特征按照F值大小排序

**参数说明：** 

输入文件training_file：svm格式文件 
输出文件 .fscore：特征排序后的结果文件 

**用法实例：**

```
python ./fselect.py training_file [testing_file]
```

**算法参考** 

`[1] Lin, H. et al. Predicting cancerlectins by the optimal g-gap dipeptides. Scientific reports 5, doi:10.1038/srep16964 (2015)` 



## BinomialDistribution（二项分布）

#### 原理：

如果每种多联体在所有的数据集中的总次数为 Mij， 那么第 j 种多联体出现在
数据集中第 i 类样本集中的 DNA 序列中的概率即为 pij，计算公式如下： 
$$
P_{ij}=\frac{m_{ij}}{M_{j}}
$$
这里 mij为第 i 类样本集中的 DNA 序列中出现第 j 种多联体的总次数。 我们用 Nj 来表示第 j 种多联体出现在所有的数据集中的总次数，则第 j 种多联体在第 i 类样本集的 DNA 序列中随机出现 nij次以及更多次的概率可以定义为： 

​                                            
$$
P(n_{ij})=\sum_{m=n_{ij}}^{N_j}\frac{N_j^!}{m!(N_j-m)}P_i^m(1-p_i)^{N_j-m}\\
$$
如果 P(nij)是一个很小的值，则意味着第 j 种多联体出现在第 i 类样本集的 DNA
序列中并不是一个随机事件。这种某种多联体便有倾向性地出现在某类样本集的
DNA 序列中的情况，其置信度可以用 CLij来描述                                                        
$$
CL_{ij}=1-P(n_{ij}）
$$

$$
CL_{ij}=max(CL_{1j},CL_{2j})
$$

最后所有特征按照置信度的值从大到小排序。

#### 用法：

- ***BinomialDistribution.py*** 

**程序说明：** 

本程序基于二项分布对8000种三肽的特征进行特征选择（支持多分类） 

**参数说明：** 

可选参数： 

-m MaxC/MinI  

MaxC表示根据每个三肽在各类中的最大CLs值进行排序[默认] 
MinI表示依据三肽在各类中的最小排序索引值进行排序 

-s sortedRank.file  

排序结果的输出文件名 

必选参数： 

pathOfFasta.txt  样本蛋白fasta序列文件的文件名【包含路径】，详见test目录下。
feature.csv  排序后的特征文件【csv格式】 

**用法实例：**

> ```
> python BinomialDistribution.py [-m MaxC/MinI][-s sortedRank.file] pathOfFasta.txt feature.csv
> ```

**算法参考** 