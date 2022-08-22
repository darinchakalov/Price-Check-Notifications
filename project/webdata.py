from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = r'https://www.ozone.bg/product/smartfon-motorola-moto-g200-5g-6-88-8gb-128gb-mirage/'

driver.get(url)

product_name = driver.find_element(By.XPATH, '//*[@id="product_addtocart_form"]/div/div[2]/h1').text
price_element = driver.find_element(By.ID, 'product-price-495247').text
price = ''
for line in price_element:
    price += line.strip()
price = float(price[:-3].replace(',', '.'))


def return_data():
    return {'product_name': product_name, 'price': price}
