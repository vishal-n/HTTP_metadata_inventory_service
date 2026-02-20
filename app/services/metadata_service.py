from fastapi import BackgroundTasks
from app.repository.metadata_repo import MetadataRepo
from app.worker.metadata_worker import collect_metadata


repo = MetadataRepo()


class MetadataService:

    async def create(self, url: str):
        await collect_metadata(url)

    async def get(self, url: str, bg: BackgroundTasks):

        data = await repo.find(url)

        if data:
            return data

        bg.add_task(collect_metadata, url)

        return None
