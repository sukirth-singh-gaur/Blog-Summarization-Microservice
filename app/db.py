
import os
from pymongo.mongo_client import MongoClient # type: ignore
from pymongo.server_api import ServerApi # type: ignore
from dotenv import load_dotenv # type: ignore
load_dotenv()
uri = os.getenv("MONGO_URI")
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["test"];

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

#print(db.list_collection_names())
blogs_collection = db["blogs"];

#
# print(blogs_collection.find_one());

# result = blogs_collection.update_many(
#     { "summary": { "$exists": False } },
#     {
#         "$set": {
#             "summary": None,
#             "summaryStatus": "LEGACY"
#         }
#     }
# )

# print("Matched:", result.matched_count)
# print("Modified:", result.modified_count)

