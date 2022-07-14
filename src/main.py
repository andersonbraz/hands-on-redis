import datetime
import redis
import uuid
import json
import time

# r = redis.StrictRedis(host="xxxxxx.cache.amazonaws.com", port=6379, db=0, password="your-key-oauth", ssl=True, ssl_cert_reqs=None)
r = redis.StrictRedis(host="localhost", port=6379, db=0, password="your-key-oauth")

def producer():
    for x in range(9999):
        data = {
            "file": str(uuid.uuid4()),
            "date": str(datetime.date.today()),
            "seq": int(x),
        }
        print(json.dumps(data))
        ikey = "key_" + str(x)
        r.hmset(ikey, data)


def consumer():
    result = r.hgetall("key_9985")
    print(result)


def clear_cache():
    r.flushall()

producer()
time.sleep(15)
consumer()

# Delete All Keys
# r.flushall()