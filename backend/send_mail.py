import smtplib
from email.message import EmailMessage

def send_email(hr_email, company, role, message):

    sender = "satiamit01@gmail.com"
    password = "mrqc mwgc keig xqsg"

    subject = f"Application for {role} at {company}"

    body = f"""
Dear Hiring Manager,

I hope you are doing well.

I would like to apply for the position of {role} at {company}.

{message}

Please find my resume attached.

Regards
Amit Sati
"""

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = hr_email
    msg.set_content(body)

    with open("resumes/resume.pdf", "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename="Amit_Sati_Resume.pdf"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)