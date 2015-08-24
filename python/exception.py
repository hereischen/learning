def fetcher(obj, index):
    return obj[index]

x = 'Spam'

if __name__ == '__main__':
    # try:
    #     fetcher(x, 4)
    # except IndexError:
    #     print 'no big deal'

    # try:
    #     raise IndexError
    # except IndexError:
    #     print "i am ok"

    # try:
    #     fetcher(x, 4)
    # finally:
    #     print ('after fetch')
    # print 'i am waiting'

    try:
        print 'hello'
    except IndexError:
        print 'done'
    else:
        print 'not yet'
