from fastapi import FastAPI, UploadFile, File
import os
import time
import aiofiles
import models
from db import engine, SessionLocal
from sqlalchemy import select
from models import Profiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def isRar(filename):
    if not filename.endswith(".rar"):
        return {"error": "Only .rar files are allowed."}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    start = time.time()
    filename = file.filename

    isRar(filename) # Check if the uploaded file has .rar extension
    
    # Define the directory to save the uploaded files
    save_directory = "./uploaded_files/"
    os.makedirs(save_directory, exist_ok=True)

    output_path = os.path.join(save_directory, filename)
    # Write file down into local
    async with aiofiles.open(output_path, "wb") as f:
        while True:
            chunk = await file.read(15000000) # 15MB per read
            if not chunk: break
            await f.write(chunk)


    end = time.time()
    processing_time = end - start
    print("Time take: " + str(round(processing_time * 10, 5)) + " seconds")
    return {"filename": filename, "message": "File uploaded successfully."}

