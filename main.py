from extract import extract
from typing import Union
import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/invoice")
async def create_file(file: UploadFile = File()):
    path = 'temp.pdf'
    with open('temp.pdf', "wb+") as file_object:
        file_object.write(file.file.read())
    vat_id, address, total = extract(path)
    response = {
                "vat_id": vat_id,
                "address": address,
                "total": total
            }
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

