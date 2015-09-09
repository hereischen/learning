class WCtrans(object):

	def __init__(self,trans_total,trans_cost):
		self.trans_total = trans_total
		self.trans_cost = trans_cost

	def __eq__(self, other):
	    if isinstance(other, self.__class__):
	        return self.__dict__ == other.__dict__
	    else:
	        return False
	def __str__(self):
		return "WCtrans object: " + str(self.__dict__)


	
a = WCtrans('123','123')
b = WCtrans('123','123')
print a==b
print a is b
print a 

d1= {'123':a}
d2= {'234':b}
print d1['123'] == d2['234']