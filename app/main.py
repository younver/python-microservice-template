from fastapi import FastAPI, HTTPException
import uvicorn

from app.models.models import Request, Response
from app.config import *


app = FastAPI()


@app.get("/health-check")
async def health_check():
    return {"status": "healthy"}

@app.post("/endpoint")
async def endpoint(request: Request) -> Response:

    try:
        some_field = request.some_field + SERVICE_KEY
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

    response = Response(some_field= some_field)
    return response


if __name__ == "__main__":
    uvicorn.run(app)
