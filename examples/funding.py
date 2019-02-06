import cardconnect # noqa

cardconnect.username = 'testing'
cardconnect.password = 'testing123'
cardconnect.base_url = 'fts.cardconnect.com:6443'
cardconnect.debug = True


print "Performing funding get ..."

resp = cardconnect.Funding.get('496160873888', '0419')

print 'Funding get response: %r' % (resp, )
