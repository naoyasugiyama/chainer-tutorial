
# coding: utf-8

# ### 

# In[33]:

import numpy as np

a = np.array([
    [0, 1, 2, 1, 0],
    [3, 4, 5, 4, 3],
    [6, 7, 8, 7, 6],
    [3, 4, 5, 4, 4],
    [0, 1, 2, 1, 0]
])
b = np.array([1, 2, 3, 4, 5])

c = np.empty((5, 5))


# # 結果を格納する配列を先に作る
# ### timeitで計測

# In[35]:

get_ipython().run_cell_magic('timeit', '', 'for i in range(a.shape[0]):\n    c[i, :] = a[i, :] + b')


# ### 

# In[36]:

c


# ### 8.9. NumPy を用いた重回帰分析

# In[37]:

# Xの定義
X = np.array([
    [2, 3],
    [2, 5],
    [3, 4],
    [5, 9],
])

X


# In[38]:

# データ数（X.shape[0]) と同じ数だけ 1 が並んだ配列
ones = np.ones((X.shape[0], 1))

# concatenate を使い、1 次元目に 1 を付け加える
X = np.concatenate((ones, X), axis=1)

# 先頭に 1 が付け加わったデザイン行列
X


# ### また、目標値が以下で与えられたとします。

# In[39]:

# t の定義
t = np.array([1, 5, 6, 8])

t


# ### 重回帰分析は、正規方程式を解くことで最適な 1 次方程式の重みを決定することができました。 正規方程式の解は以下のようなものでした。
# ### todo 数式の書き方を調べる
# 
# これを、4 つのステップに分けて計算していきます。
# 
# まずは、XTX の計算です。ndarrayに対して .T で転置した配列を得られます。
# 
# 

# In[40]:

# Step 1
xx = np.dot(X.T, X)

xx


# ### 次に、この逆行列を計算します。

# In[41]:

# Step 2
xx_inv = np.linalg.inv(xx)

xx_inv


# 逆行列の計算は np.linalg.inv() で行うことができます。
# 
# 次に、XTt の計算をします。
# 
# 

# In[43]:

# Step 3
xt = np.dot(X.T, t)

xt


# 最後に、求めた xx_inv と xt を掛け合わせます。
# 
# 

# In[44]:

# Step 4
w = np.dot(xx_inv, xt)

w


# 実際には逆行列を陽に求めることは稀で、連立一次方程式を解く、すなわち逆行列を計算してベクトルに掛けるのに等しい計算をひとまとめに行う関数 numpy.linalg.solve を呼ぶ方が速度面でも精度面でも有利です。

# In[45]:

w_ = np.linalg.solve(X.T.dot(X), X.T.dot(t))

w_


# In[5]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt

price = [100, 250, 350, 489, 680]
number = [ x for x in range(5) ]

# wirte graph
plt.plot(price, number)

# graph title
plt.title("price / number")

# x lable
plt.xlabel("price")

# y label
plt.ylabel("number")

# draw
plt.show()


# In[ ]:



