import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from App3 import password

# Step 1: Scrape quotes from a website
def scrape_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = []
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            quotes.append(f"{text} - {author}")
        return quotes
    else:
        print(f"Failed to retrieve quotes. Status code: {response.status_code}")
        return []

# Step 2: Send an email
def send_email(smtp_server, smtp_port, smtp_user, smtp_password, to_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(smtp_user, to_email, text)
    server.quit()

# Step 3: Main function to scrape quotes and send them via email
def main():
    # Website to scrape
    url = "http://quotes.toscrape.com/"
    quotes = scrape_quotes(url)

    if not quotes:
        print("No quotes found. Exiting...")
        return

    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'blessingechukwunwike@gmail.com'
    smtp_password = password
    if not smtp_user or not smtp_password:
        print("SMTP credentials are not set. Please set the SMTP_USER and SMTP_PASSWORD environment variables.")
        return

    # List of recipients
    recipients = ['blessingeugwuegbu@gmail.com', 'davidinmichael@gmail.com']

    # Send each quote as an email
    for quote in quotes:
        for recipient in recipients:
            send_email(smtp_server, smtp_port, smtp_user, smtp_password, recipient, "Daily Quote", quote)
            print(f"Sent quote to {recipient}")
            time.sleep(60)  # Wait for 1 minute between sending emails

if __name__ == "__main__":
    main()