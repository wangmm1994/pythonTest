import redis
pool = redis.ConnectionPool(host='193.112.31.175', port=6379)
conn = redis.Redis(connection_pool=pool)

conn.hset('n1','t1', 'Hello World')
conn.hset('n1','t2', 'Hello')

