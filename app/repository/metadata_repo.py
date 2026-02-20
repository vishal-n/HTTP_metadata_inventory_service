from app.database import metadata_collection


class MetadataRepo:

    async def find(self, url: str):
        return await metadata_collection.find_one({"url": url})

    async def save(self, data: dict):
        await metadata_collection.update_one(
            {"url": data["url"]},
            {"$set": data},
            upsert=True
        )
