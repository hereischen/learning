# -*- coding: utf-8 -*-
from numpy import *
import operator

def create_dataset():
	group = array([[1.0,1.1], [1.0,1.0], [0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels


def classify0(inX, dataset, labels, k):
	# 计算距离
	dataset_size =  dataset.shape[0]  # shape[rows, cols]
	diff_mat = tile(inX,(dataset_size,1)) - dataset
	sq_diff_mat = diff_mat**2
	sq_distances = sq_diff_mat.sum(axis=1)
	distances = sq_distances**0.5
	sorted_dist_indicies = distances.argsort()
	class_count = {}
	# 选择距离最小的k个点
	for i in range(k):
		voteI_label = labels[sorted_dist_indicies[i]]
		class_count[voteI_label] = class_count.get(voteI_label,0) + 1
	# 排序
	sorted_class_count = sorted(class_count.iteritems(),key=operator.itemgetter(1), reverse=True)
	return sorted_class_count[0][0]

if __name__ == '__main__':
	group,labels = create_dataset()
	print classify0([0,0],group,labels,2)
