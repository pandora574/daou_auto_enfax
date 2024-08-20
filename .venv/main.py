import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None

def execChrome():
    global driver
    driver = webdriver.Chrome() #크롬 드라이버 런타임 경로 지정
    driver.maximize_window()
    driver.get("https://devfanta.enfax.com:14172/") #엔팩스 사이트 접속
    print("사이트 접속")

def Login_Page_click():
    global driver
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/span/a").click()
    print("로그인 페이지 이동 클릭")

def ID_sends():
    global driver
    driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys("justin7929")
    print("아이디 입력")

def PW_sends():
    global driver
    driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys("asdf!123")
    print("비밀번호 입력")

def Login_click():
    global driver
    driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
    print("로그인 클릭")

def Later_click():
    global driver
    driver.find_element(By.XPATH, '//*[@id="btnChangeNext"]').click()
    print("다음에 변경하기 클릭")

def Message_click():
    global driver
    driver.find_element(By.XPATH, '//*[@id="topWrapper"]/div[1]/div[1]/div/div[2]/ul[1]/li[3]/strong').click()
    print("문자발송 메뉴 클릭")

def Message_send_click():
    global driver
    driver.find_element(By.XPATH, '//*[@id="topWrapper"]/div[1]/div[1]/div/div[2]/ul[1]/li[3]/div/div/div[1]').click()
    print("문자 보내기 클릭")


execChrome()
Login_Page_click()
time.sleep(0.3)
ID_sends()
time.sleep(0.3)
PW_sends()
time.sleep(1)
Login_click()
time.sleep(1)
Later_click()
time.sleep(1)
Message_click()
time.sleep(0.3)
Message_send_click()
time.sleep(0.5)