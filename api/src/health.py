from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
import json

router = APIRouter()

@router.get("/health")
async def get_location(request: Request) -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={
            "error": False,
            "message": "Service healthy.",
            "payload": {}
        }
    )