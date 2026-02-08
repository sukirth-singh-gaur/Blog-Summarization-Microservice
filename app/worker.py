from rq import Worker, Queue
from app.redis_conn import redis_conn

listen = ["blog-summary"]

if __name__ == "__main__":
    queues = [Queue(name, connection=redis_conn) for name in listen]
    worker = Worker(queues, connection=redis_conn)
    worker.work()
