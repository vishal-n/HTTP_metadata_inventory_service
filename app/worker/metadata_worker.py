import httpx
from app.repository.metadata_repo import MetadataRepo


repo = MetadataRepo()


async def collect_metadata(url: str):

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(url)

        metadata = {
            "url": url,
            "headers": dict(response.headers),
            "cookies": dict(response.cookies),
            "page_source": response.text
        }

        await repo.save(metadata)
