from fastapi import FastAPI
from pydantic import BaseModel
import smtplib
from email.message import EmailMessage
import os

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://portfolio-stp5.onrender.com"],  # ton frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactForm(BaseModel):
    name: str
    email: str
    subject: str
    message: str

@app.post("/contact")
def send_contact(form: ContactForm):

    msg = EmailMessage()
    msg["Subject"] = f"Portfolio Contact: {form.subject}"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = "zinsouconstanta@gmail.com"

    msg.set_content(f"""
    Nom: {form.name}
    Email: {form.email}

    Message:
    {form.message}
    """)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)

    return {"status": "Message envoyé avec succès"}


@app.get("/")
def home():
    return {"message": "Portfolio Contact API is running"}