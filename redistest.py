import redis

client = redis.Redis(socket='/home/u222914/redis.sock')

client.set('Language', 'Python')
print client.get('Language')

client.sadd('pythonlist', 'value1', 'value2', 'value3')
print client.smembers('pythonlist')
client.sadd('redislist', 'value1', 'value5', 'value6', 'value7', 'value8')
print "sinter", client.sinter('pythonlist', 'redislist')
print "sunion", client.sunion('pythonlist', 'redislist')
print client.scard('pythonlist')

client.hset('Person', 'Name', 'Person1')
client.hset('Person', 'Health', '600')
client.hset('Person', 'Mana', '200')
print client.hgetall('Hero')

