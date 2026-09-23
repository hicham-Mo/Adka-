from __future__ import annotations

import json
from typing import Any

import httpx

from backend.agent import build_fallback_response, build_system_prompt
from backend.config import GEMINI_API_KEY, GROQ_API_KEY, ANTHROPIC_API_KEY


async def call_provider(model: str, expert_name: str, prompt: str) -> dict[str, Any]:
    model_key = model.lower().strip()

    if model_key == "groq":
        return await call_groq(prompt, expert_name)
    if model_key == "gemini":
        return await call_gemini(prompt, expert_name)
    if model_key == "claude":
        return await call_claude(prompt, expert_name)

    raise ValueError(f"النموذج غير مدعوم: {model}")


async def call_groq(prompt: str, expert_name: str) -> dict[str, Any]:
    if not GROQ_API_KEY:
        return {
            "response": build_fallback_response("groq", expert_name, prompt),
            "provider": "groq",
            "status": "fallback",
        }

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": build_system_prompt(expert_name)},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        res = await client.post(url, headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
        text = data["choices"][0]["message"]["content"]
        return {"response": text, "provider": "groq", "status": "ok"}


async def call_gemini(prompt: str, expert_name: str) -> dict[str, Any]:
    if not GEMINI_API_KEY:
        return {
            "response": build_fallback_response("gemini", expert_name, prompt),
            "provider": "gemini",
            "status": "fallback",
        }

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "system_instruction": {"parts": [{"text": build_system_prompt(expert_name)}]},
        "contents": [{"parts": [{"text": prompt}]}],
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        res = await client.post(url, json=payload)
        res.raise_for_status()
        data = res.json()
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        return {"response": text, "provider": "gemini", "status": "ok"}


async def call_claude(prompt: str, expert_name: str) -> dict[str, Any]:
    if not ANTHROPIC_API_KEY:
        return {
            "response": build_fallback_response("claude", expert_name, prompt),
            "provider": "claude",
            "status": "fallback",
        }

    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 1024,
        "system": build_system_prompt(expert_name),
        "messages": [{"role": "user", "content": prompt}],
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        res = await client.post(url, headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
        text = data["content"][0]["text"]
        return {"response": text, "provider": "claude", "status": "ok"}
