from rq import Queue# type: ignore
from app.redis_conn import redis_conn
from app.jobs import summarize_blog

queue = Queue("blog-summary", connection=redis_conn)

def push_blog_id(blog_id: str):
    queue.enqueue(
        summarize_blog,
        blog_id,
    )
