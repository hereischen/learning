l = [2, 23, 4, 1, 13, 9, 12, 10, 7]

def bubble_sort(l):
	for passnum in xrange(len(l)-1,0,-1):
		for i in xrange(passnum):
			if l[i] > l[i+1]:
				l[i], l[i+1] = l[i+1],l[i]
	return l

def selection_sort(l):
	for passnum in xrange(len(l)-1,0,-1):
		index_of_max = 0
		for i in xrange(1, passnum +1):
			if l[i] > l[index_of_max]:
				index_of_max = i
		l[passnum],l[index_of_max] = l[index_of_max], l[passnum]
	return l

def insertion_sort(l):
	for index in xrange(1,len(l)):
		current_value = l[index]
		position = index

		while position > 0 and l[position-1] > current_value:
			l[position] = l[position-1]
			position = position -1
		l[position] = current_value
	return l


if __name__ == '__main__':
	# print bubble_sort(l) 
	# print selection_sort(l)	
	print insertion_sort(l)		
