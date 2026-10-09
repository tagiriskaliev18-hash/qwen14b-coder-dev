# ⚡ Qwen 2.5 Coder 14B · Local AI Developer

> Часть экосистемы **[MindTagSystem](https://github.com/tagiriskaliev18-hash/MindTagSystem)** · автор **Тагир Искалиев** ([@tagiriskaliev18-hash](https://github.com/tagiriskaliev18-hash))

> **100% Автономная, быстрая локальная модель для разработки ПО на базе Qwen 2.5 Coder 14B (квантование Q3_K_M, полная загрузка 49 слоев в GPU).**
> Включает готовый Modelfile, скрипт установки в 1 клик и полнофункциональный современный веб-интерфейс чата с подсветкой синтаксиса и стримингом.

---

## 🚀 Возможности и характеристики

- **Архитектура:** Qwen 2.5 Coder 14B Instruct
- **Квантование:** `Q3_K_M` (~7.3 GB) — максимальная точность при низком расходе видеопамяти.
- **Аппаратное ускорение:** 49 из 49 слоев выгружаются прямо в GPU (оптимизировано под NVIDIA RTX 3070 8GB, а также любые карты с 8GB+ VRAM).
- **Контекст:** 4096 токенов.
- **Инженерная специализация:**
  - Полный рабочий код без сокращений, заглушек и `TODO`.
  - Backend (FastAPI, Flask, Django, Node.js, Go).
  - Frontend (HTML5 Canvas, React, Vue, CSS).
  - Скрипты автоматизации, парсеры и боты.
  - Алгоритмы, архитектура и оптимизация производительности.
- **Веб-интерфейс:**
  - Стильная темная тема (GitHub Dark / modern slate).
  - Стриминг ответов в реальном времени.
  - Подсветка синтаксиса кода с кнопками быстрого копирования.
  - Настройка температуры и контекста на лету.

---

## ⚡ Быстрый запуск в 1 клик

### Для Windows:
Просто запустите двойным кликом файл:
```bat
setup_and_run.bat
```
*Скрипт автоматически проверит Ollama, скачает модель, соберет `qwen14b`, установит зависимости Python и откроет браузер на `http://127.0.0.1:8008`.*

### Для Linux / macOS:
```bash
chmod +x setup_and_run.sh
./setup_and_run.sh
```

---

## 🛠 Ручная установка (3 шага)

Если вы хотите запустить всё вручную:

### 1. Установите базовую модель в Ollama:
```bash
ollama pull qwen2.5-coder:14b-instruct-q3_K_M
```

### 2. Соберите оптимизированную модель из Modelfile:
```bash
ollama create qwen14b -f Modelfile
```

### 3. Установите зависимости и запустите сервер:
```bash
pip install -r requirements.txt
python server.py
```
После запуска откройте в браузере: **`http://127.0.0.1:8008`**

---

## 📋 Структура проекта

```
qwen14b-coder-dev/
├── Modelfile              # Конфигурация модели с инструкцией Senior-разработчика
├── index.html             # Современный веб-интерфейс чата с Markdown и подсветкой
├── server.py              # Быстрый FastAPI сервер со стримингом через Ollama
├── setup_and_run.bat      # Лаунчер в 1 клик для Windows
├── setup_and_run.sh       # Лаунчер в 1 клик для Linux/macOS
├── requirements.txt       # Зависимости Python
└── README.md              # Документация
```

---

## 🎯 Пример запросов к модели

- *"Напиши полноценный REST API на FastAPI с JWT авторизацией, базой данных SQLite и Pydantic-схемами."*
- *"Создай законченную браузерную игру на HTML5 Canvas с анимациями и звуками в одном файле без внешних библиотек."*
- *"Реализуй многопоточный асинхронный парсер на Python с ротацией прокси, повторными запросами и экспортом в SQLite."*

---

## 🌐 Часть экосистемы MindTagSystem

Qwen 14B Coder Dev входит в **[MindTagSystem](https://github.com/tagiriskaliev18-hash/MindTagSystem)** — экосистему для программистов, которую создаёт **Тагир Искалиев** ([@tagiriskaliev18-hash](https://github.com/tagiriskaliev18-hash)): своя операционная система, браузер, IDE, ИИ-ядро и приложения, которые работают вместе и которые можно встроить в любое устройство.

**Роль в экосистеме:** локальная модель для программирования (слой «ИИ-ядро»).

| Слой | Проект | Что делает |
|---|---|---|
| Платформа | [AIsktagOS](https://github.com/tagiriskaliev18-hash/AisktagOS) | Операционная система для разработчиков в стиле macOS на любом железе |
| Инструменты разработчика | [Mind IDE](https://github.com/tagiriskaliev18-hash/Mind-IDE) | ИИ-среда разработки: один чат с моделями, Claude Code и Antigravity |
| Инструменты разработчика | [ITIS Browser](https://github.com/tagiriskaliev18-hash/ITIS-browser) | Браузер с ИИ-агентом, который сам кликает и листает страницы |
| ИИ-ядро | [AI Duo (multimodel-agent)](https://github.com/tagiriskaliev18-hash/multimodel-agent) | Единый ИИ-шлюз с OpenAI-совместимым API для всех моделей |
| ИИ-ядро | [Antigravity ↔ Claude Code Bridge](https://github.com/tagiriskaliev18-hash/antigravity-claude-bridge) | MCP-мост, который связывает Antigravity, Claude Code и пул моделей |
| ИИ-ядро | **Qwen 14B Coder Dev** ← вы здесь | Локальная офлайн-модель для программирования в Ollama |
| Приложения | [FileHub AI](https://github.com/tagiriskaliev18-hash/filehub-ai) | Хранилище файлов с ИИ-агентом для Word, PowerPoint и Excel |
| Приложения | [SortApp (анализатор логов)](https://github.com/tagiriskaliev18-hash/sortapp) | Анализатор журналов доступа к сетевым папкам с отчётами Excel |
| Приложения | [ИИ Доктор (medical-ai-assistant)](https://github.com/tagiriskaliev18-hash/medical-ai-assistant) | Офлайн-ассистент врача приёмного покоя |

Как проекты связаны между собой: [архитектура MindTagSystem](https://github.com/tagiriskaliev18-hash/MindTagSystem/blob/main/docs/ARCHITECTURE.md). Автор всех проектов экосистемы — Тагир Искалиев.
