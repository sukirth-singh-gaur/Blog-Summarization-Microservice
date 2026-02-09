import os
from fastapi import FastAPI, HTTPException, Header#type:ignore
from rq import Queue #type:ignore
from app.redis_conn import redis_conn

app = FastAPI()
queue = Queue("blog-summary", connection=redis_conn)

#INTERNAL_TOKEN = os.getenv("INTERNAL_TOKEN")


@app.post("/summarize/{blog_id}")
#def summarize(blog_id: str, authorization: str = Header(None)):
def summarize(blog_id: str):
    # if authorization != f"Bearer {INTERNAL_TOKEN}":
    #     raise HTTPException(status_code=401, detail="Unauthorized")

    job = queue.enqueue(
        "app.jobs.summarize_blog",
        blog_id,
        retry=[10, 30, 60],
        job_timeout=300,
        result_ttl=500,
    )

    return {
        "status": "queued",
        "job_id": job.id,
    }
