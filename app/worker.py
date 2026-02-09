from rq import Worker, Queue#type:ignore
from app.redis_conn import redis_conn
import os
os.environ["GRPC_ENABLE_FORK_SUPPORT"] = "0"

listen = ["blog-summary"]

if __name__ == "__main__":
    queues = [Queue(name, connection=redis_conn) for name in listen]
    worker = Worker(queues, connection=redis_conn)
    worker.work()
