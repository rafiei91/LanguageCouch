# LanguageCouch

LanguageCouch is an AI-powered language learning application that generates complete Language lessons using Google's Gemini models.

## Features

- AI-generated dialogues
- Vocabulary extraction
- Multi-speaker audio
- Conversation mode
- Shadowing mode
- Learning mode
- JSON lesson storage

## Technologies

- Python
- Google Gemini API
- Gemini TTS
- Pydantic
- FastAPI (planned)
- React (planned)

## Installation

```bash
git clone https://github.com/<your-user>/LanguageCouch.git
cd LanguageCouch

conda create -n danishcoach python=3.11
conda activate danishcoach

pip install -r requirements.txt
```

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key
```

Run:

```bash
python main.py
```

## Roadmap

- ✅ Lesson generation
- ✅ Vocabulary generation
- ✅ Multi-speaker audio
- ✅ Shadowing mode
- ✅ Learning mode
- ⏳ FastAPI backend
- ⏳ React frontend
- ⏳ Mobile PWA
