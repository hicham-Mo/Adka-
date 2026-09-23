from __future__ import annotations

from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from backend.config import APP_TITLE, APP_VERSION, get_allowed_origins
from backend.providers import call_provider

app = FastAPI(title=APP_TITLE, version=APP_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    model: str = Field(default="groq", min_length=2, max_length=20)
    expert: str = Field(default="أمر عام", min_length=1, max_length=100)
    prompt: str = Field(..., min_length=1, max_length=20000)


@app.get("/health")
async def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "service": APP_TITLE,
        "version": APP_VERSION,
    }


@app.post("/api/query")
async def query(req: QueryRequest) -> dict[str, Any]:
    try:
        result = await call_provider(req.model, req.expert, req.prompt)
        return {
            "response": result["response"],
            "model": req.model,
            "expert": req.expert,
            "provider": result["provider"],
            "status": result["status"],
        }
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=500, detail=f"فشل في معالجة الاستدعاء: {exc}") from exc


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "نور الاستخلاف يعمل بنجاح."}
