
STRING = 'receiver=&pswd=&msgid=1000909181755566700&reportTime=1509091818&mobile=18513645088&status=DELIVRD'

s = STRING.split('&')
test = [[1, 2], [3, 4]]

print dict(test)

d = dict(x.split('=') for x in STRING.split('&'))
print d
l = [x.split('=') for x in STRING.split('&')]
print l
