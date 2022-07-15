import datetime
import telnetlib
import redis
import uuid
import json
from telnetlib import Telnet

host_redis = "localhost"
ip_redis = "127.0.0.1"
token = ""

r = redis.Redis(
        host=host_redis, 
        port=6379, 
        db=0, 
        password=token, 
        ssl=True, 
        ssl_cert_reqs=None
    )

def producer():
    for x in range(10):
        data = {
            "file": str(uuid.uuid4()),
            "date": str(datetime.date.today()),
            "seq": int(x),
        }
        print(json.dumps(data))
        ikey = "key_" + str(x)
        r.hmset(ikey, data)


def consumer():
    result = r.hgetall("key_5")
    print(result)


def clear_cache():
    print("Flush Data on Redis!")
    r.flushall()

def check_connection():
    try:
        r.ping()
        print("Successfully connected to redis")
    except (telnetlib):
        print("Redis connection error!")
        return False
    return True

def check_telnet():
    tn = telnetlib.Telnet()
    try:
        tn.open(ip_redis, 6379, 30)
        tn.write(b"Hello!")
        response = 'Success Telnet!'
    except Exception:
        response = 'Failed Telnet!'
    finally:
        tn.close()
        print(response)
        
# Check Telnet
check_telnet()
# Check Connection Redis
check_connection()
# Call Producer
producer()
# Call Consumer
consumer()
# Delete All Keys
clear_cache()
