from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .routers import upload, events, products, webhooks
from .database import engine, Base
from . import models
import os

app = FastAPI(title="Product Importer")

models.Base.metadata.create_all(bind=engine)

app.include_router(upload.router)
app.include_router(events.router)
app.include_router(products.router)
app.include_router(webhooks.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def root():
    return FileResponse(os.path.join("app", "static", "index.html"))

@app.get("/health")
async def health_check():
    return {"status": "ok"}

os.makedirs("uploads", exist_ok=True)
