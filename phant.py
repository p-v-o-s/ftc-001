import urllib2
from random import randint
import time 

# replace these keys with those appropriate to your feed on data.sparkfun.com
publicKey='9JyZ00pQg7iDyOYaWDrv'
privateKey='xz4y55b8R1tbm5owZb47'

#publicKey='xR0W4ZM6vpCO4waYNRzA'
#privateKey='ZaevwqAKzrS2WmJoE89n'

while 1:

    # create a random number (in future, could be a measurement)
    r = randint(1,10)/10.

    print r

    # here, we're calling our parameter 'rando':

    sentence = 'https://data.sparkfun.com/input/'+str(publicKey)+'?private_key='+str(privateKey)+'&rando='+str(r)

    url_response = urllib2.urlopen(sentence)

    print url_response

    time.sleep(20) 

