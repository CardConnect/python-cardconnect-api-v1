import cardconnect # noqa

cardconnect.username = 'testing'
cardconnect.password = 'testing123'
cardconnect.base_url = 'fts.cardconnect.com:6443'
cardconnect.debug = True


print "Performing void ..."

resp = cardconnect.Void.create(
    merchid='496160873888',
    retref='109858246936'
)

print 'Void response: %r' % (resp, )
