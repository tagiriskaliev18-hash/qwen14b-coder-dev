@echo off
chcp 65001 >nul
title Qwen 2.5 Coder 14B - 1-Click Setup and Launcher

echo =====================================================================
echo  ⚡ Qwen 2.5 Coder 14B (Q3_K_M) - Локальная среда разработки
echo =====================================================================
echo.

:: 1. Проверка наличия Ollama
where ollama >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [!] Ollama не найдена в PATH!
    echo     Пожалуйста, скачайте и установите Ollama с официального сайта:
    echo     https://ollama.com/download
    pause
    exit /b 1
)

:: 2. Проверка запущен ли сервер Ollama
curl -s http://127.0.0.1:11434/api/tags >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [*] Запуск службы Ollama...
    start "" ollama serve
    timeout /t 3 /nobreak >nul
)

:: 3. Проверка базовой квантованной модели Qwen 14B Q3_K_M
echo [*] Проверка модели qwen2.5-coder:14b-instruct-q3_K_M в Ollama...
ollama list | findstr /i "qwen2.5-coder:14b-instruct-q3_K_M" >nul
if %ERRORLEVEL% neq 0 (
    echo [*] Загрузка квантованной модели (Q3_K_M, ~7.3GB)...
    ollama pull qwen2.5-coder:14b-instruct-q3_K_M
    if %ERRORLEVEL% neq 0 (
        echo [!] Ошибка при загрузке модели. Проверьте интернет-соединение.
        pause
        exit /b 1
    )
)

:: 4. Создание оптимизированной GPU-модели qwen14b
echo [*] Сборка локальной модели qwen14b из Modelfile...
ollama create qwen14b -f Modelfile
if %ERRORLEVEL% neq 0 (
    echo [!] Ошибка при сборке qwen14b.
    pause
    exit /b 1
)

:: 5. Проверка Python и установка зависимостей
echo [*] Проверка окружения Python...
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [!] Python не найден! Установите Python 3.10+ с сайта https://python.org
    pause
    exit /b 1
)

echo [*] Установка зависимостей (fastapi, uvicorn, httpx)...
python -m pip install -r requirements.txt --quiet

:: 6. Запуск веб-сервера и открытие интерфейса
echo.
echo =====================================================================
echo  ✅ Всё готово! Запуск сервера разработчика на http://127.0.0.1:8008
echo =====================================================================
echo.

start "" "http://127.0.0.1:8008"
python server.py

pause
