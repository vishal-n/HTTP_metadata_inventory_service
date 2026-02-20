from fastapi import APIRouter, BackgroundTasks, status
from app.models.metadata_model import URLRequest
from app.services.metadata_service import MetadataService


router = APIRouter()
service = MetadataService()


@router.post("/metadata")
async def create_metadata(req: URLRequest):
    await service.create(str(req.url))
    return {"message": "Metadata collected"}


@router.get("/metadata")
async def get_metadata(url: str, bg: BackgroundTasks):

    data = await service.get(url, bg)

    if data:
        return data

    return {
        "status": status.HTTP_202_ACCEPTED,
        "message": "Metadata collection initiated"
    }
