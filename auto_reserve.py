from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def check():
    table = driver.find_element(By.CLASS_NAME, "p-reservation_customer_table")
    tbody = table.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")
    for table_cell in range(len(trs)):
        td = trs[table_cell].find_elements(By.TAG_NAME, "td")
        for i in range(len(td)):
            try:
                sleep(0.2)
                js = "document.getElementsByClassName('hidden')[1].click()"
                driver.execute_script(js)
                driver.find_element(By.XPATH,
                                    "/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/button").click()
                break

            except:
                print("クリックできる要素が見つかりません。")
                td[i].click()


options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

options.use_chromium = True

driver = webdriver.Chrome(resource_path('driver/chromedriver.exe'), options=options)

driver.get("https://omakase.in/users/sign_in")

driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[1]/form/div[1]/input").send_keys(
    input("メールアドレスを入力して下さい"))

driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[1]/form/div[2]/input").send_keys(
    input("パスワードを入力して下さい。"))

driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[1]/form/input[2]").click()

driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[1]/form/div/div[3]/div/input").send_keys(
    input("検索するお店を入力してください。"))


driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[1]/form/div/div[4]/input").click()

# driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/a/div[2]/h4").click()
js = "document.getElementsByClassName('ui button primary big fluid')[0].click()"
driver.execute_script(js)

driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/a").click()

sleep(1)
check()
