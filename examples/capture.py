import cardconnect # noqa

cardconnect.username = 'testing'
cardconnect.password = 'testing123'
cardconnect.base_url = 'fts.cardconnect.com:6443'
cardconnect.debug = True


print "Performing capture ..."

resp = cardconnect.Capture.create(
    merchid='496160873888',
    retref='110776233356'
)

print 'Capture response: %r' % (resp, )
