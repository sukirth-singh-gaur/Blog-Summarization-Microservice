import os# type: ignore
import redis# type: ignore
from dotenv import load_dotenv# type: ignore

load_dotenv()

redis_conn = redis.Redis(
    host=os.getenv("REDIS_HOST_URL"),
    port=os.getenv("REDIS_PORT"),   
    username="default",
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,                 
)

redis_conn.ping()                                 
print("Redis connected!")

redis_conn.set("foo", "bar")
print(redis_conn.get("foo"))
