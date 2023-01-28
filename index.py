from fastapi import FastAPI
from routes.users import user
from docs import tags_metadata

app = FastAPI(
    title="FastAPI with mongo",
    description="This is a simple rest api with FastAPI and MongoDB",
    version="1.0.0",
    openapi_tags=tags_metadata
)

app.include_router(user)
