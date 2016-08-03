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

def file2matrix(filename):
	fr = open(filename)
	array_olines = fr.readlines()
	nnumber_of_lines = len(array_olines)
	return_mat = zeros((nnumber_of_lines,3))
	class_label_vector = []

	index = 0
	for line in array_olines:
		line = line.strip()
		list_form_line = line.split('\t')
		return_mat[index,:] = list_form_line[0:3]
		# class_label_vector.append(list_form_line[-1])
		class_label_vector.append(int(list_form_line[-1]))
		index+=1
	return return_mat,class_label_vector

def auto_norm(dataset):
	min_vals = dataset.min(0)
	max_vals = dataset.max(0)
	ranges = max_vals - min_vals
	norm_dataset = zeros(shape(dataset)) # 根据原有数据，创建全项为0的新数据
	m = dataset.shape[0]
	norm_dataset = dataset - tile(min_vals, (m,1))
	norm_dataset = dataset/ tile(ranges, (m,1))
	return norm_dataset, ranges, min_vals

def dating_class_test():
	ho_ratio = 0.10
	dating_data_mat, dating_labels=file2matrix('datingTestSet2.txt')
	norm_mat, ranges, min_vals = auto_norm(dating_data_mat)
	m = norm_mat.shape[0]
	# 取10%作为测试数据，剩余为训练数据
	num_test_vecs = int(m*ho_ratio)
	error_count = 0.0
	for i in range(num_test_vecs):
		classifier_result = classify0(norm_mat[i,:], norm_mat[num_test_vecs:m,:],
			dating_labels[num_test_vecs:],3)
		print "the classifier came back with: %d, the real answer is: %d" % (classifier_result, dating_labels[i])

		if (classifier_result != dating_labels[i]):
			error_count+= 1.0
	print "the total error rate is: %f " % (error_count/float(num_test_vecs))

def classify_person():
	result_list = ['不可能', '较低可能', '很大可能']
	percent_tats = float(raw_input("玩游戏的时间比例？"))
	ff_miles = float(raw_input("每年飞行历程？"))
	icecream = float(raw_input("每年吃多少升冰淇凌？"))
	dating_data_mat, dating_labels=file2matrix('datingTestSet2.txt')
	norm_mat, ranges, min_vals = auto_norm(dating_data_mat)
	in_arr = array([percent_tats,ff_miles,icecream])
	classifier_result = classify0((in_arr - min_vals)/ranges, norm_mat, dating_labels,3)
	print '你喜欢这个人的可能性为: ', result_list[classifier_result-1]


if __name__ == '__main__':
	group,labels = create_dataset()
	# print classify0([0,0],group,labels,2)
	# dating_class_test()
	classify_person()



