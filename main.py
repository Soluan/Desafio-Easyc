from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def main():
    DRIVER_PATH = './chromedriver.exe'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get('https://best.aliexpress.com/?lan=en&spm=a2g0o.productlist.1000002.1.4b647581Vk3WWl&gatewayAdapt=glo2bra')
    sleep(15)  

    pesquisa(driver)

    coletando_dados()

def pesquisa(driver):
    driver.find_element(By.NAME, "SearchText").send_keys("redmi")
    sleep(5)
    driver.find_element('xpath', '//*[@id="form-searchbar"]/div[1]/input').click()


def coletando_dados():
    soup = BeautifulSoup(site.content, 'html.parser')
    redmi = soup.find_all('div', class_= '_3t7zg _2f4Ho')


