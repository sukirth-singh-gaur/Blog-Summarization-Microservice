from app.db import blogs_collection
from app.summarizer import generate_summary
from bson import ObjectId# type: ignore
import logging

logging.basicConfig(level=logging.INFO)

def summarize_blog(blog_id: str):
    blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})

    if not blog:
        raise ValueError("Blog not found")

    if blog.get("summaryStatus") == "COMPLETED":
        logging.info("Summary already completed")
        return

    logging.info("Generating summary...")

    try:
        summary = generate_summary(blog["content"])

        blogs_collection.update_one(
            {"_id": blog["_id"]},
            {
                "$set": {
                    "summary": summary,
                    "summaryStatus": "COMPLETED",
                }
            },
        )

    except Exception as e:
        logging.error(f"Failed summary for {blog_id}: {e}")

        blogs_collection.update_one(
            {"_id": blog["_id"]},
            {"$set": {"summaryStatus": "FAILED"}}
        )
        raise
