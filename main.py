# from fastapi import FastAPI
# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
from database import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()


# Define a directory to save images
UPLOAD_DIR = "./uploads/"

os.makedirs(UPLOAD_DIR, exist_ok=True)


# meta = MetaData()
#
# meta.create_all(engine)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_path": file_path}



