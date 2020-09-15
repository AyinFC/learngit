#!/usr/bin/env python
# coding: utf-8

# # 调用函数库

# In[17]:
# sklearn.tree.DecisionTreeClassifier()参数说明
# https://www.cnblogs.com/hgz-dm/p/10886368.html

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression


# # 数据加载

# In[2]:


digits = load_digits()
data = digits.data


# # 数据探索

# In[3]:


#print(data)
print(data.shape)
print(digits.images[0])
print(digits.target[0])


# In[4]:


#plt.gray()
plt.imshow(digits.images[0])
# 画出图像，但不显示
plt.show()
# 显示图像


# # 划分训练集与测试集

# In[7]:


x_train,x_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.25, random_state=33)
#random_state：随机种子值


# # 规范化

# In[8]:


ss = preprocessing.StandardScaler()
x_train_ss = ss.fit_transform(x_train)
x_test_ss = ss.transform(x_test)


# # 构建模型

# In[16]:


cart = DecisionTreeClassifier(criterion='gini')
cart.fit(x_train_ss, y_train)
#训练模型
predict_y = cart.predict(x_test_ss)
#预测
print('CART准确率为：{}'.format(accuracy_score(predict_y, y_test)))
#评估


# # 创建LR分类器

# In[18]:


lr = LogisticRegression()
lr.fit(x_train_ss, y_train)
predict_y=lr.predict(x_test_ss)
print('LR准确率: %0.4lf' % accuracy_score(predict_y, y_test))

