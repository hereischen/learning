from io import StringIO, BytesIO
f = StringIO()
f.write(u'hello')
f.write(u' ')
f.write(u'world!')
print (f.getvalue())

b = BytesIO()
b.write('BytesIO'.encode('utf-8'))
print(b.getvalue())
