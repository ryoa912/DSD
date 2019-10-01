import redis

conn = redis.Redis()
print(conn.hincrby('test', 'count'))
print(conn.hincrby('test', 'count', 10))
print(conn.hincrby('test', 'count', 100))

# result
# {b'count': b'1', b'name': b'Fester Bestertester'}
