# 0x02. Redis basic

## Resources

[redis commands](https://redis.io/commands/)

## Connecting to redis -python

[redis-py](https://redis-py.readthedocs.io/en/stable/)

- Assuming you run Redis on localhost:6379 (the default)

```
import redis
r = redis.Redis()
r.ping()
```

- Running redis on foo.bar.com, port 12345

```
import redis
r = redis.Redis(host='foo.bar.com', port=12345)
r.ping()
```
