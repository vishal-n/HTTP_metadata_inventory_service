from fastapi import FastAPI
from app.api.metadata_routes import router
from app.database import metadata_collection


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """Create indexes on application startup."""
    try:
        await metadata_collection.create_index("url", unique=True)
    except Exception as e:
        # Log but don't fail startup if index creation fails (e.g., auth issues)
        print(f"Warning: Could not create index: {e}")


app.include_router(router)
