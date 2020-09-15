import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder


#data = pd.read_csv('test.csv', header=None)
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header=None)

transactions = []
for i in range(0, dataset.shape[0]):
	temp = []
	for j in range(0, dataset.shape[1]):
		if str(dataset.values[i,j]) != 'nan':
			temp.append(str(dataset.values[i,j]))
		#print(temp)
		transactions.append(temp)

#print(transactions)

'''
lists = data.values.tolist()

# 去除NAN项
for trac in lists:
	while np.NAN in trac:
		trac.remove(np.NAN)

print('trac:', trac)
print('lists:', lists)
'''

te = TransactionEncoder()
te_one_hot = te.fit_transform(transactions)
df = pd.DataFrame(te_one_hot, columns=te.columns_)

frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=0.5)

print('频繁项集:', frequent_itemsets)
print('关联规则:', rules[(rules['lift'] >= 1)])

