from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from domain.user import user_router

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

app.mount("/assets",StaticFiles(directory="front/assets")) 

@app.get("/")
async def root():
   return FileResponse("front/index.html")


