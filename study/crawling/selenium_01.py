from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://comic.naver.com/index")

time.sleep(2)

webtoonMenu = driver.find_element(by=By.XPATH, value='//*[@id="menu"]/li[2]/a')
webtoonMenu.click()

time.sleep(2)

dayList = ["월", "화", "수", "목", "금", "토", "일"]

for day in dayList:
    webtoonDayMenus = driver.find_elements(by=By.CSS_SELECTOR, value='.SubNavigationBar__link--PXX5B')

    for menu in webtoonDayMenus:
        if menu.text != day:
            continue

        menu.click()

        time.sleep(2)

        scrollTop = 0
        while True:
            driver.execute_script(f"window.scrollTo(0, {scrollTop})")

            scrollTop += 500
            time.sleep(1)
            if scrollTop > driver.execute_script("return document.body.scrollHeight"):
                break