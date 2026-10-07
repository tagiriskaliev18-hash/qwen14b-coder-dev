#!/usr/bin/env bash
set -e

echo "====================================================================="
echo "  ⚡ Qwen 2.5 Coder 14B (Q3_K_M) - Local AI Developer Setup"
echo "====================================================================="
echo ""

# 1. Check Ollama
if ! command -v ollama &> /dev/null; then
    echo "[!] Ollama is not installed. Please install it from https://ollama.com"
    exit 1
fi

# 2. Check Ollama running
if ! curl -s http://127.0.0.1:11434/api/tags > /dev/null 2>&1; then
    echo "[*] Starting Ollama serve..."
    ollama serve &
    sleep 3
fi

# 3. Pull base quantized model
echo "[*] Pulling base model qwen2.5-coder:14b-instruct-q3_K_M..."
ollama pull qwen2.5-coder:14b-instruct-q3_K_M

# 4. Create custom model
echo "[*] Creating custom model qwen14b from Modelfile..."
ollama create qwen14b -f Modelfile

# 5. Install dependencies
echo "[*] Installing Python dependencies..."
python3 -m pip install -r requirements.txt --quiet

# 6. Launch server
echo ""
echo "====================================================================="
echo "  ✅ Ready! Server launching at http://127.0.0.1:8008"
echo "====================================================================="
echo ""

python3 server.py
