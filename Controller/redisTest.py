import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
conn = redis.Redis(connection_pool=pool)

conn.hset('n1','t1', 'Hello World')
conn.hset('n1','t2', 'Hello')

