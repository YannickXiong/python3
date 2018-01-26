def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(csm):
    csm.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = csm.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    csm.close()


c = consumer()
produce(c)
