from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from time import sleep


def check():
    table = driver.find_element(By.CLASS_NAME, "p-reservation_customer_table")
    tbody = table.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")
    for table_cell in range(len(trs)):
        td = trs[table_cell].find_elements(By.TAG_NAME, "td")
        for i in range(len(td)):
            try:
                js = "document.getElementsByClassName('hidden')[1].click()"
                sleep(1)
                driver.execute_script(js)
                driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/button").click()
                break

            except:
                print("クリックできる要素が見つかりません。")
                td[i].click()


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get("https://omakase.in/users/sign_in")

driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[1]/form/div[1]/input").send_keys(
    input("メールアドレスを入力して下さい"))

driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[1]/form/div[2]/input").send_keys(
    input("パスワードを入力して下さい。"))

driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[1]/form/input[2]").click()

driver.execute_script("window.open('https://omakase.in/ja/r/qn865701');")

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/a").click()
sleep(2)

check()
