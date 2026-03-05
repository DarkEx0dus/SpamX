#!/usr/bin/env python3

import smtplib
import random
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import subprocess

def check_install(command, install_command):
    result = subprocess.run(f"which {command}", shell=True, stdout=subprocess.PIPE)
    if result.stdout.decode().strip() == "":
        print(f"[+] Installing {command}...")
        os.system(install_command)
    else:
        print(f"[✓] {command} already installed.")

def install_dependencies():
    os.system("pkg update -y")
    check_install("figlet", "pkg install figlet -y")
    check_install("ruby", "pkg install ruby -y")
    check_install("lolcat", "gem install lolcat")

def banner():
    os.system("clear")
    os.system("figlet SPAMX | lolcat")

    print("""created by: DarkEx0dus """)

def main():
    install_dependencies()
    banner()

    print("Program started...")


def load_html(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()


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
