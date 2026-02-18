from fastapi import FastAPI

app = FastAPI(title="HTTP Metadata Inventory Service")


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to HTTP Metadata Inventory Service"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
