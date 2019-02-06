import cardconnect # noqa

cardconnect.username = 'testing'
cardconnect.password = 'testing123'
cardconnect.base_url = 'fts.cardconnect.com:6443'
cardconnect.debug = True


print "Performing auth ..."

resp = cardconnect.Auth.create(
    merchid='496160873888',
    account='4111111111111111',
    expiry='1218',
    amount='1.00',
    currency='USD'
)

print 'Auth response: %r' % (resp, )
