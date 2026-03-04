#!/usr/bin/env python3

import smtplib
import random
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# =========================
# BANNER
# =========================
def banner():
    print(r"""
███████╗██████╗    █████╗   ███╗       ███╗   ██╗  ██╗
██╔════╝██╔══██╗██╔══██╗████╗   ████║╚██╗██╔╝
███████╗██████╔╝███████║██╔████╔██║  ╚███╔╝ 
╚════██║██╔═══╝  ██╔══██║██║╚██╔╝██║  ██╔██╗ 
███████║██║            ██║     ██║██║ ╚═╝    ██║██╔╝ ██╗
╚══════╝╚═╝            ╚═╝     ╚═╝╚═╝            ╚═╝╚═╝    ╚═╝

Created By: Andrew Cadiz
""")

# =========================
# LOAD HTML
# =========================
def load_html(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

# =========================
# SEND EMAIL
# =========================
def send_mail(server, port, email, password, receiver, subject, html):

    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.login(email, password)

    msg = MIMEMultipart("alternative")
    msg["From"] = email
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.attach(MIMEText(html, "html"))

    smtp.sendmail(email, receiver, msg.as_string())
    smtp.quit()

# =========================
# MAIN
# =========================
def main():

    banner()

    receiver = input("target email: ")
    html_file = "test.html"
    count = int(input("How many emails to send: "))

    smtp_server = "smtp.gmail.com"
    port = 587

    sender = input("Sender Gmail: ")
    password = input("App Password: ")

    html_content = load_html(html_file)

    print(f"\n[+] Sending {count} spamming emails...\n")

    for i in range(count):
        send_mail(
            smtp_server,
            port,
            sender,
            password,
            receiver,
            "Cybersecurity ",
            html_content
        )

        print(f"[+] Sent target email {i+1}")
        time.sleep(1)

    print("\n[✓] Spam Complete.")

if __name__ == "__main__":
    main()