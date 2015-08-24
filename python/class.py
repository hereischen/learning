from itertools import ifilterfalse
from decimal import Decimal as D


class WCtrans(object):

    def __init__(self, trans_total, trans_cost):
        self.trans_total = trans_total
        self.trans_cost = trans_cost
        self.status = 'matching'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            flg = (self.__dict__ == other.__dict__)
            print other.__dict__
            if (self.__dict__['trans_total'] != other.__dict__['trans_total']
                    and self.__dict__['trans_cost'] != other.__dict__['trans_cost']):
                self.status = 'both'
            elif self.__dict__['trans_total'] != other.__dict__['trans_total']:
                self.status = 'total'
            elif self.__dict__['trans_cost'] != other.__dict__['trans_cost']:
                self.status = 'cost'
            return flg
        else:
            return False

    def __str__(self):
        return "WCtrans object: " + str(self.__dict__)


a = WCtrans('122', '12')
b = WCtrans('123', '123')
print a == b
print a is b
print a

d1 = {'1': 6, '2': 2}
d2 = {'1': 5, '2': 3}
d3 = {'1': 6, '2': 2}
L = list(set(d1.keys()) & set(d2.keys()))
print L
temp_dict = {}
temp_dict['01'] = []
temp_dict['10'] = [1111111, 222222, 3333, 4444, 5555]
temp_dict['02'] = []
temp_dict['20'] = []
for k in L:
    if d1[k] < d2[k]:
        temp_dict['02'].append(k)
    elif d1[k] > d2[k]:
        temp_dict['20'].append(k)

print 'shit'
print temp_dict

for key in temp_dict.keys():
    if temp_dict[key] != []:
        diff_type = key
        print diff_type
        for transaction_no in temp_dict[key]:
            print transaction_no

# d3.update(temp_dict)
# print d3

# for (k, v) in d1.items():
#     if

# print d2.keys()
# f = set(d1.keys()) - set(d2.keys())
# # print d1 == d2
# print [x for x in d1.keys() if x not in d2.keys()]
# print [x for x in d2.keys() if x not in d1.keys()]

# for x in (d1.keys(), d2.keys()):
#     print x

# d1.update(d2)
# print d1

# r = list(ifilterfalse(lambda x: x in d1, d2))
# R = list(ifilterfalse(lambda x: x in d2, d1))
# print r, R

x = D('0.01')
y = D('0.02')

a = True
print not a
