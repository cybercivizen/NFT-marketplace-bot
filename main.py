import threading
import time
from time import sleep
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def setup_wallet(driver):
    phrase = 'SEED PHRASE HERE'
    password = 'PASSWORD HERE'

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input'))).send_keys(phrase)

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH,'//*[@id="password"]'))).send_keys(password)

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="confirm-password"]'))).send_keys(password)

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/form/button'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="popover-content"]/div/div/section/header/div/button'))).click()


def setup_harmony(driver):
    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/button'))).click()

    # NETWORK NAME
    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input'))).send_keys('Harmony Mainnet 0 POKT Portal ')

    # NEW RPC URL
    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input'))).send_keys('https://harmony-0-rpc.gateway.pokt.network')

    # CHAIN ID
    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input'))).send_keys('1666600000')

    # CURRENCY SYMBOL
    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input'))).send_keys('ONE')

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]'))).click()


def connect_wallet(driver):
    sleep(2)
    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/header/div/div/div[2]/div'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[3]/div/div/div[2]'))).click()

    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/notification.html#connect/2d662c3c-a464-4968-ab03'
               '-f4af0bfa7550')

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]'))).click()


def buy_plot(driver):
    print('Buying the plot...')

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/div/div[4]/div/div[1]'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/div/div[6]/div[2]/div[1]'))).click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[7]/div'))).click()

    print('Confirming transaction...')
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])

    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[2]'))).click()

    print('Transaction confirmed, plot bought!')


def fetch_floor_price(driver):
    global counter
    while True:
        try:
            driver.get(
                'https://nftkey.app/collections/wenlambonft/?marketplaceTab=listings&sorterType=listingPrice&sortDirection=asc')

            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1aoett')))

            market_floor_price = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/div/div[1]/div[2]/div/div[2]/div[3]/div[1]'))).text

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            counter = counter + 1

            print(f'[{counter}] [{current_time}] Floor price: ' + market_floor_price)

            if float(market_floor_price.replace(',', '').replace(' ONE', '')) <= user_floor_price:
                buy_plot(driver)
        except Exception:
            continue


def main():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')
    options.add_extension("MetaMask.crx")
    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    setup_wallet(driver)
    setup_harmony(driver)
    sleep(4)
    driver.close()
    driver.switch_to.window(windows[0])
    driver.get(
        'https://nftkey.app/collections/wenlambonft/?marketplaceTab=listings&sorterType=listingPrice&sortDirection=asc')
    connect_wallet(driver)
    fetch_floor_price(driver)


counter = 0
user_floor_price = 500
thread_list = []

for i in range(2):
    t = threading.Thread(name='INSTANCE [{}]'.format((i + 1)), target=main)
    t.start()
    time.sleep(0.25)
    print(t.name + ' started!')
    thread_list.append(t)

# Wait for all threads to complete
for thread in thread_list:
    thread.join()






