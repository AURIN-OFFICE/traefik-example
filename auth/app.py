from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
import os

app = FastAPI()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@app.get("/")
async def auth_check(request: Request):
    auth_header = request.headers.get("Authorization")

    if auth_header == "Bearer letmein":
        resp = Response(status_code=200)
        resp.headers["X-Forwarded-Google-Api-Key"] = GOOGLE_API_KEY
        return resp
    return JSONResponse(status_code=401, content={"error": "Unauthorized"})

