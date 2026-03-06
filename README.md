# MindGuard - AI Mental Health Early Detection & Support System

MindGuard is a comprehensive, state-of-the-art mental health support platform that leverages AI, machine learning, and interactive design to provide early emotional risk detection and personalized support.

## 🚀 Vision
To address the critical gaps in mental health care—such as incomplete symptom alleviation, patient attrition, and loss of follow-up—by providing a modern, interactive, and privacy-first digital companion.

---

## ✨ Key Features

### 🧩 Smart Diagnostics & Tracking
- **Clinical Assessments**: Integrated PHQ-9 and GAD-7 questionnaires with automated interpretation.
- **Image MCQ Test**: A unique, non-verbal mood assessment using a pool of emotion-mapped images.
- **Voice Emotional Tracking**: Real-time acoustic feature extraction (pitch, energy, speed) to detect subtle emotional shifts during interactions.
- **Sentiment Analysis**: Continuous monitoring of chat conversations to provides a "Wellbeing Score" and "Risk Level."

### 🎙️ AI Voice Avatar Assistant (Jarvis-style)
- **Live Interaction**: A WebGL/Canvas-powered animated avatar that responds to voice input.
- **STT/TTS Integration**: Seamless speech-to-text and text-to-speech for a hands-free, human-like experience.
- **Visual Waveform Rendering**: Real-time audio waveform visualization during listening and speaking phases.

### 🎮 Stress Buster Games Hub
- **Zen Bubble Pop**: A relaxing clicking game with soft neon effects.
- **Neon Memory Match**: Improves cognitive focus through glowing card pairs.
- **Breath Harmony**: A guided visual breathing exercise (Inhale/Exhale/Hold).
- **Retro Neon Snake**: A nostalgia-driven distraction with a futuristic aesthetic.

### 📺 Personalized Mood Media
- **AI Recommendations**: Automatically suggests Tamil media content (songs and movies) based on your current detected mood category (Silent, humor, Motivated, etc.).
- **Interactive Grid**: Modern recommendation cards with direct YouTube playback.

### 🍃 Wellness Hub
- **Journaling**: A private space for reflection with a "Share with AI" feature to transition journal entries into support conversations.
- **Interactive Affirmations**: Daily positive reinforcement based on mood trends.

### 📊 Advanced Dashboard
- **Data Visualization**: Real-time Chart.js graphs for Wellbeing Trends and Mood Distribution.
- **Persistent BGM**: Meditation background music that syncs across page transitions with mute control.
- **Style Toggle**: Switch between a vibrant **Neon Mode** and a cleaner **Normal Mode** at the click of a button.

---

## 🛠️ Tech Stack

- **Backend**: Python / Flask
- **Frontend**: HTML5, Tailwind CSS, Vanilla JS
- **Database**: SQLite (SQLAlchemy)
- **ML Engine**: Scikit-Learn (Sentiment Analysis & Risk Prediction)
- **Visuals**: WebGL, Canvas API, Bootstrap Icons
- **Auth**: Google OAuth & Traditional Email/Password
- **Networking**: Flask-Dance for OAuth, CSRF Protection

---

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Mental-Health-Detector
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file from the `.env.example` template:
   ```bash
   cp .env.example .env
   # Add your Secret Key, Google OAuth Credentials, etc.
   ```

5. **Initialize the Database**:
   ```bash
   python run_seed.py  # Seeds images and initial data
   ```

6. **Run the application**:
   ```bash
   python run.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

---

## 🔒 Privacy & Safety
- **Data Anonymization**: Session identifiers are used instead of PII in core analysis engines.
- **Automated Wiping**: Conversation transcripts are wiped from generated PDF reports before download to ensure total privacy.
- **Safety Helplines**: Persistent access to crisis helplines in the template footer.
- **Anti-Inspect**: Protection against basic client-side code scraping (Right-click/F12 protection).

---

## ⚖️ Disclaimer
MindGuard is an AI-based support tool and **not a substitute for professional medical advice**, diagnosis, or treatment. It is designed for early detection and emotional support. In case of a crisis, please contact your local emergency services or the helplines provided in the footer.
