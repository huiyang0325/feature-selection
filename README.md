# Feature selection

## F-Score

#### 原理：

F-Score 是度量特征在不同类别间的区分度的一种指标， F-Score值越大， 代表该特征在不同类别之间的区分度越强 . 假设 x_k 代表数据集中的样本（k = 1,2,…,N） . n+为正类样本的数量， n-为负类样本的数量， 则数据集中第i个特征的F-Score可由



![F_i=\frac{(\bar{x}_i^{(+)}-\bar{x}_i)^2+(\bar{x}_i^{(-)}-\bar{x}_i)^2}{\frac{1}{n_+-1}\sum_{k=1}^{n_+}(x_{k,i}^{(+)}-\bar{x}_i^{(+)})^2+\frac{1}{n_{-}-1}\sum_{k=1}^{n_{-}}(x_{k,i}^{(-)}-\bar{x}_i^{(-)})^2}](http://latex.codecogs.com/gif.latex?F_i%3D%5Cfrac%7B%28%5Cbar%7Bx%7D_i%5E%7B%28&plus;%29%7D-%5Cbar%7Bx%7D_i%29%5E2&plus;%28%5Cbar%7Bx%7D_i%5E%7B%28-%29%7D-%5Cbar%7Bx%7D_i%29%5E2%7D%7B%5Cfrac%7B1%7D%7Bn_&plus;-1%7D%5Csum_%7Bk%3D1%7D%5E%7Bn_&plus;%7D%28x_%7Bk%2Ci%7D%5E%7B%28&plus;%29%7D-%5Cbar%7Bx%7D_i%5E%7B%28&plus;%29%7D%29%5E2&plus;%5Cfrac%7B1%7D%7Bn_%7B-%7D-1%7D%5Csum_%7Bk%3D1%7D%5E%7Bn_%7B-%7D%7D%28x_%7Bk%2Ci%7D%5E%7B%28-%29%7D-%5Cbar%7Bx%7D_i%5E%7B%28-%29%7D%29%5E2%7D)



#### 用法：

- ***Fscore.py*** 

**程序说明：** 

使用Fscore的原理对输入特征按照F值大小排序

**参数说明：** 

输入文件training_file：svm格式文件 
输出文件 .fscore：特征排序后的结果文件 

**用法实例：**

```
python ./fscore.py training_file [testing_file]
```



## ANOVA（方差分析）

#### 原理：

用于两个及两个以上样本均数差别的显著性检验。



F值就是组间方差和组内方差的比值，这个F值越大意味着某个特征具有更好的区分正负样本的能力。因此，所有的特征都可以根据这个F值进行排序。

![F(\xi)=\dfrac{s_{B}^{2}(\xi)}{s_{W}^{2}(\xi)}](http://latex.codecogs.com/gif.latex?F%28%5Cxi%29%3D%5Cdfrac%7Bs_%7BB%7D%5E%7B2%7D%28%5Cxi%29%7D%7Bs_%7BW%7D%5E%7B2%7D%28%5Cxi%29%7D)



**组间方差**，即水平之间的方差，是衡量不同总体下各样本之间差异的方差。

![s_B^2(\xi)=\sum_{i=1}^{K}m_i\frac{\left ( \frac{\sum_{j=1}^{m_i}f_{\xi}^g(i,j)}{m_i}-\frac{\sum_{i=1}^{K}\sum_{j=1}^{m_i}f_{\xi}^g(i,j)}{\sum_{i=1}^{K}m_i} \right )^2}{df_B}](http://latex.codecogs.com/gif.latex?s_B%5E2%28%5Cxi%29%3D%5Csum_%7Bi%3D1%7D%5E%7BK%7Dm_i%5Cfrac%7B%5Cleft%20%28%20%5Cfrac%7B%5Csum_%7Bj%3D1%7D%5E%7Bm_i%7Df_%7B%5Cxi%7D%5Eg%28i%2Cj%29%7D%7Bm_i%7D-%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7BK%7D%5Csum_%7Bj%3D1%7D%5E%7Bm_i%7Df_%7B%5Cxi%7D%5Eg%28i%2Cj%29%7D%7B%5Csum_%7Bi%3D1%7D%5E%7BK%7Dm_i%7D%20%5Cright%20%29%5E2%7D%7Bdf_B%7D)

简化公式后可以看成

![s_B^2(\xi)=\sum_{i=1}^{K}m_i\frac{\left ( \bar{x_i}-\bar{x} \right )^2}{df_B}](http://latex.codecogs.com/gif.latex?s_B%5E2%28%5Cxi%29%3D%5Csum_%7Bi%3D1%7D%5E%7BK%7Dm_i%5Cfrac%7B%5Cleft%20%28%20%5Cbar%7Bx_i%7D-%5Cbar%7Bx%7D%20%5Cright%20%29%5E2%7D%7Bdf_B%7D)

**组内方差**，即水平内部的方差，是衡量同一个总体下样本数据的方差。

![s_W^2(\xi)=\sum_{i=1}^{K}\sum_{j=1}^{m_i}\frac{\left ( f_{\xi}^g(i,j)-\frac{\sum_{j=1}^{m_i}f_{\xi}^g(i,j)}{m_i} \right )^2}{df_W}](http://latex.codecogs.com/gif.latex?s_W%5E2%28%5Cxi%29%3D%5Csum_%7Bi%3D1%7D%5E%7BK%7D%5Csum_%7Bj%3D1%7D%5E%7Bm_i%7D%5Cfrac%7B%5Cleft%20%28%20f_%7B%5Cxi%7D%5Eg%28i%2Cj%29-%5Cfrac%7B%5Csum_%7Bj%3D1%7D%5E%7Bm_i%7Df_%7B%5Cxi%7D%5Eg%28i%2Cj%29%7D%7Bm_i%7D%20%5Cright%20%29%5E2%7D%7Bdf_W%7D)

简化公式后可以看成

![s_W^2(\xi)=\sum_{i=1}^{K}\sum_{j=1}^{m_i}\frac{\left (x_{ij}-\bar{x_i} \right )^2}{df_W}](http://latex.codecogs.com/gif.latex?s_W%5E2%28%5Cxi%29%3D%5Csum_%7Bi%3D1%7D%5E%7BK%7D%5Csum_%7Bj%3D1%7D%5E%7Bm_i%7D%5Cfrac%7B%5Cleft%20%28x_%7Bij%7D-%5Cbar%7Bx_i%7D%20%5Cright%20%29%5E2%7D%7Bdf_W%7D)



#### 用法：

- ***ANOVA.py*** 

**程序说明：** 

使用方差分析思想对输入特征进行共线性大小排序

**参数说明：** 

-i 输入文件，csv格式文件 
-o 输出文件，特征排序后的结果文件 

**用法实例：**

```
python ANOVA.py -i test.csv -o result.anova
```



## BinomialDistribution（二项分布）

#### 原理：

如果每种多联体在所有的数据集中的总次数为 Mij， 那么第 j 种多联体出现在
数据集中第 i 类样本集中的 DNA 序列中的概率即为 pij，计算公式如下： 

![P_{ij}=\frac{m_{ij}}{M_{j}}](http://latex.codecogs.com/gif.latex?P_%7Bij%7D%3D%5Cfrac%7Bm_%7Bij%7D%7D%7BM_%7Bj%7D%7D)


$$
P_{ij}=\frac{m_{ij}}{M_{j}}
$$
这里 mij为第 i 类样本集中的 DNA 序列中出现第 j 种多联体的总次数。 我们用 Nj 来表示第 j 种多联体出现在所有的数据集中的总次数，则第 j 种多联体在第 i 类样本集的 DNA 序列中随机出现 nij次以及更多次的概率可以定义为： 



![P(n_{ij})=\sum_{m=n_{ij}}^{N_j}\frac{N_j^!}{m!(N_j-m)}P_i^m(1-p_i)^{N_j-m}\\](http://latex.codecogs.com/gif.latex?P%28n_%7Bij%7D%29%3D%5Csum_%7Bm%3Dn_%7Bij%7D%7D%5E%7BN_j%7D%5Cfrac%7BN_j%5E%21%7D%7Bm%21%28N_j-m%29%7DP_i%5Em%281-p_i%29%5E%7BN_j-m%7D%5C%5C)

​                                            

如果 P(nij)是一个很小的值，则意味着第 j 种多联体出现在第 i 类样本集的 DNA序列中并不是一个随机事件。这种某种多联体便有倾向性地出现在某类样本集的DNA 序列中的情况，其置信度可以用 CLij来描述   



![P_{ij}=\frac{m_{ij}}{M_{j}}](http://latex.codecogs.com/gif.latex?P_%7Bij%7D%3D%5Cfrac%7Bm_%7Bij%7D%7D%7BM_%7Bj%7D%7D)

​                                          

​                                                                            ![CL_{ij}=1-P(n_{ij})](http://latex.codecogs.com/gif.latex?CL_%7Bij%7D%3D1-P%28n_%7Bij%7D%29)



![CL_{ij}=max(CL_{1j},CL_{2j})](http://latex.codecogs.com/gif.latex?CL_%7Bij%7D%3Dmax%28CL_%7B1j%7D%2CCL_%7B2j%7D%29)



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



## CSV文件，SVM文件互相转换

- csvtosvm.py

```
python csvtosvm.py test.csv test.svm
```

- svmtocsv.py

```
python svmtocsv.py test.svm test.csv
```

