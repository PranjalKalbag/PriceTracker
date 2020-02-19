import requests
from bs4 import BeautifulSoup
import smtplib
import time
#TURN OFF GOOGLE SECURE APPS FOR MAIL TO SEND EMAIL NOTIFICATIONS
URL = ''
#URL of product whose price needs to be tracked
URL = input("Enter Amazon URL: ")
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"}
#Defines type of browser. Can search for my user agent on the browser to find
def check_price():
    page  = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    print(title.strip())

    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price = float(price[2:4]+price[5:8])
    #convert string to number. Change list index according to product
    print(converted_price)
    if(converted_price<50000.0):#change base price as required
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('username', 'password') #change username and password
    subject = 'Price Drop ALert!'

    body = 'Check link: https://www.amazon.in/dp/B07DJ8K2KT?pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e&pf_rd_r=R3VSW0PQ285BR1T2SN7B '
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'sender address',   #address of the email sender 
        'recv address',     #address of the email reciever
         msg                #message to be sent
    )
    print('Email Sent!')
    server.quit()
while True:
    check_price()
    time.sleep(3600)
    