import cardconnect # noqa

cardconnect.username = 'testing'
cardconnect.password = 'testing123'
cardconnect.base_url = 'fts.cardconnect.com:6443'
cardconnect.debug = True


print "Performing profile creation ..."

resp = cardconnect.Profile.create(
    merchid='496160873888',
    account='9418594164541111',
    name='Test User'
)

print 'Profile creation response: %r' % (resp, )

print "Performing profile update ..."

resp = cardconnect.Profile.update(
    merchid='496160873888',
    profile='13106769609077182008',
    account='9418594164541111',
    name='Test User Updated',
    profileupdate='Y'
)

print 'Profile update response: %r' % (resp, )

print "Performing profile get ..."

resp = cardconnect.Profile.get('13106769609077182008', '496160873888')

print 'Profile get response: %r' % (resp, )

print "Performing profile deletion ..."

resp = cardconnect.Profile.delete('13106769609077182008', '496160873888')

print 'Profile deletion response: %r' % (resp, )
