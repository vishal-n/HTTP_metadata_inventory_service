from app.database import metadata_collection
from bson import ObjectId


class MetadataRepo:

    async def find(self, url: str):
        doc = await metadata_collection.find_one({"url": url})
        if doc:
            # Remove _id field (ObjectId) for JSON serialization
            doc.pop("_id", None)
        return doc

    async def save(self, data: dict):
        await metadata_collection.update_one(
            {"url": data["url"]},
            {"$set": data},
            upsert=True
        )
