import smtplib

from bs4 import BeautifulSoup
import requests
headers = {
    'Accept-Language':'',
    'User-Agent':'',
}
url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
user_id = ''
password = ''
response = requests.get(url=url,headers=headers)
result = response.text

soup = BeautifulSoup(result,'html.parser')
price = float(soup.find(class_="a-price-whole").get_text())

if price <= 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user_id,password=password)
        connection.sendmail(from_addr=user_id,
                            to_addrs='',
                            msg=f'Subject:Amazon Price Alert \n\n Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart is now {price}.'.encode('UTF-8'))