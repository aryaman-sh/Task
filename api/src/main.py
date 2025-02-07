from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .health import router as health_router
from .autosuggest import router as autosuggest_router

app = FastAPI()

# Allow all
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router) # Health for service healthcheck
app.include_router(autosuggest_router)