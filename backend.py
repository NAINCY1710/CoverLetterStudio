import os, tempfile
from datetime import date
from dotenv import load_dotenv
from fpdf import FPDF
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise EnvironmentError("Add GEMINI_API_KEY to your .env file")

genai.configure(api_key = API_KEY)
MODEL = genai.GenerativeModel("gemini-1.5-flash")

def make_prompt(name, job_role, company, education, skills, highlights, tone, words):
    today = date.today().strftime("%B %d, %Y")
    return f'''
Date: {today}

Write a {tone.lower()} cover letter of about {words} words.

Context
-------
Applicant : {name}
Target role : {job_role}
Company : {company}
Education : {education}
Top skills : {skills}
Career wins : {highlights}

Instructions
------------
• Address the letter to the hiring team at {company}.
• Mention ONE or TWO achievements from “Career wins”.
• Explain how the applicant's skills will benefit the role.
• Close with a short thank-you and appropriate sign-off.
• Keep the letter professional and concise.
'''

def letter_to_pdf(name, text):
    safe_name = "".join(c for c in name if c.isalnum() or c in (' ', '_')).strip() or "cover_letter"
    file_name = f"{safe_name}.pdf"
    temp_dir = tempfile.gettempdir()
    path = os.path.join(temp_dir, file_name)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    for line in text.splitlines():
        pdf.multi_cell(0, 8, line)
    pdf.output(path)
    return path

def generate_letter(name, job_role, company, education, skills, highlights, tone, words):
    prompt = make_prompt(name, job_role, company, education, skills, highlights, tone, words)
    response = MODEL.generate_content(
        prompt,
        safety_settings = {
            "HARASSMENT": "block_none",
            "HATE": "block_none"
        }
    )
    letter = response.text.strip()
    pdf_path = letter_to_pdf(name, letter)
    return letter, pdf_path