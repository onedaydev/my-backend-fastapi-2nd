from typing import List

from fastapi import APIRouter, UploadFile


router = APIRouter(
    tags = ["FileUpload"]
)


@router.post("/files/")
async def create_upload_files(files: List[UploadFile]):
    for file in files:
        contents = await file.read()
        with open("./uploaded_files/{file.filename}", "wb") as f:
            f.write(contents)
    
    return {"filename": file.filename}

