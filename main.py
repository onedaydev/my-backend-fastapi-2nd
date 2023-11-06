import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from domain.user import user_router
from domain.backgroundtasks import backgroundtasks_router
from domain.upload_file import file_upload_router
from domain.post import post_router

tags_metadata = [
    {
        "name" : "user",
        "description" : "",
        "externalDocs": {
            "description" : "User external docs",
            "url" : "https://github.com/2e16Jun/my-backend-fastapi-2nd/blob/main/Obsidian%20Vault/User.md",
        },
    },
]

app = FastAPI(
    title="MyFastAPI",
    description = "",
    summary="",
    version="0.0.1",
    terms_of_service="",
    contact = {
    },
    license_info = {
        "name": "",
        "identifier" : "MIT",
    },
    openapi_tags=tags_metadata,
    #docs_url=None,
    #redoc_url=None,
)


app.include_router(user_router.router)
app.include_router(backgroundtasks_router.router)
app.include_router(file_upload_router.router)
app.include_router(post_router.router)

app.mount("/assets",StaticFiles(directory="front/assets")) 

@app.get("/")
async def root():
   return FileResponse("front/index.html")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

