"""
FastAPI Server for Local Qwen 2.5 Coder 14B.
Direct high-speed streaming inference via Ollama.
"""

import sys
import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# UTF-8 encoding fix for Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
PORT = int(os.getenv("PORT", "8008"))

app = FastAPI(title="Qwen 2.5 Coder 14B Local Server", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    html_file = Path(__file__).parent / "index.html"
    if html_file.exists():
        return FileResponse(html_file)
    return JSONResponse({"status": "ok", "message": "Qwen 2.5 Coder 14B Server Active"})

@app.get("/api/health")
async def health():
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{OLLAMA_HOST}/api/tags")
            if resp.status_code == 200:
                return {"status": "online", "ollama": True, "models": [m.get("name") for m in resp.json().get("models", [])]}
    except Exception as e:
        return {"status": "degraded", "ollama": False, "error": str(e)}
    return {"status": "unknown"}

@app.get("/api/models")
async def get_models():
    """Возвращает список доступных моделей для разработки."""
    models = [
        {
            "name": "⚡ Qwen 2.5 Coder 14B (Q3_K_M · RTX 3070 GPU)",
            "model": "qwen14b"
        },
        {
            "name": "🚀 Qwen 2.5 Coder 7B (Быстрый локальный)",
            "model": "qwen2.5-coder:7b"
        }
    ]
    try:
        async with httpx.AsyncClient(timeout=4.0) as client:
            resp = await client.get(f"{OLLAMA_HOST}/api/tags")
            if resp.status_code == 200:
                installed = [m.get("name") for m in resp.json().get("models", [])]
                # Dynamic matching
                matched = []
                for m in models:
                    if any(m["model"] in inst for inst in installed):
                        matched.append(m)
                if matched:
                    return {"models": matched}
    except Exception:
        pass
    return {"models": models}

@app.post("/api/chat")
async def chat_endpoint(request: Request):
    body = await request.json()
    model = body.get("model", "qwen14b")
    messages = body.get("messages", [])
    user_options = body.get("options", {})

    options = {
        "temperature": float(user_options.get("temperature", 0.3)),
        "num_ctx": int(user_options.get("num_ctx", 4096)),
        "repeat_penalty": 1.1,
        "top_p": 0.95
    }

    ollama_payload = {
        "model": model,
        "messages": messages,
        "stream": True,
        "options": options
    }

    async def stream_generator():
        try:
            async with httpx.AsyncClient(timeout=300.0) as client:
                async with client.stream("POST", f"{OLLAMA_HOST}/api/chat", json=ollama_payload) as resp:
                    if resp.status_code != 200:
                        err_text = await resp.aread()
                        err_msg = json.dumps({
                            "message": {
                                "role": "assistant",
                                "content": f"⚠️ Ошибка вызова Ollama ({resp.status_code}): {err_text.decode('utf-8', errors='ignore')}"
                            }
                        }) + "\n"
                        yield err_msg.encode("utf-8")
                        return

                    async for line in resp.aiter_lines():
                        if not line.strip():
                            continue
                        yield (line + "\n").encode("utf-8")
        except Exception as e:
            err_msg = json.dumps({
                "message": {
                    "role": "assistant",
                    "content": f"\n\n⚠️ Ошибка подключения к серверу Ollama: {str(e)}"
                }
            }) + "\n"
            yield err_msg.encode("utf-8")

    return StreamingResponse(stream_generator(), media_type="application/x-ndjson")

if __name__ == "__main__":
    print(f"Starting Qwen 2.5 Coder 14B Developer Server on http://127.0.0.1:{PORT}")
    uvicorn.run(app, host="127.0.0.1", port=PORT)
