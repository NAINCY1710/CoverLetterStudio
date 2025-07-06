# 💼 AI Cover Letter Studio

A simple web app to create podcast scripts and generate voiceovers with the help of IBM Watson AI services

---

## 🚀 Features

- ✍️ Generate cover letters tailored to your job, company and skills using Gemini AI
- 📄 Download as PDF with your name as the filename
- 🖊️ Edit the letter directly in the app before downloading or copying
- ⚡ Minimalistic responsive web interface built with Gradio

---

## 🧠 Powered By

- **Google Gemini 1.5 Flash AI** for generating relevant and concise cover letter content
- **FPDF** for creating high-quality PDF files
- **Gradio** for a fast, interactive and accessible frontend

---

## 💻 Setup

```bash
git clone https://github.com/NAINCY1710/CoverLetterStudio.git
cd CoverLetterStudio
python -m venv venv
venv\Scripts\activate         # for Windows
source venv/bin/activate      # for Linux/macOS
pip install -r requirements.txt
python app.py
```

---

## 🔐 Configuration
Before running the app, add your Gemini API key to a `.env file` in the project root
```bash
GEMINI_API_KEY = "your_gemini_api_key"
```

---

## 👨‍💻 Contributors

- [Naincy Jain](https://www.linkedin.com/in/naincy-jain-38a20a283)
- [Aarjav Jain](https://www.linkedin.com/in/bharatwalejain)