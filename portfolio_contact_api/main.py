from fastapi import FastAPI
from pydantic import BaseModel
import smtplib
from email.message import EmailMessage
import os

app = FastAPI()

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

    return {"status": "Message sent successfully"}