from telnetlib import STATUS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import argparse
import sys



def register_and_check_email_availability(emails):

    driver = webdriver.Chrome()

    """EdgeService = Service(
        r"C:\\tools\\msedgedriver.exe")
    driver = webdriver.Edge(service=EdgeServsice)"""

    driver.get("https://1login.wp.pl/rejestracja?client_id=poczta_nh&flow=registration&login_challenge=Cj0KJDEyMjVhMDFiZDg2NmQ2MDJiYjljOGQzMzJlZDE4YmYzYmRiMhCr-N-sBhoPCglwb2N6dGFfbmgSAnYxEiDGeDpJwzZYgINhQW4PYVNoxeveya2QOp8lHc_Hz_IDYQ&registrationFlow=newForced&registrationBrand=wpc")

    # Wprowadź dane rejestracji (zakładam, że to jest przykład)
    driver.find_element(By.NAME, 'name').send_keys("Imie")
    driver.find_element(By.NAME, "lastName").send_keys("Nazwisko")
    driver.find_element(By.NAME, "sex").send_keys("M")
    driver.find_element(By.ID, "date").send_keys("6")
    select_month = driver.find_element(By.ID, "month")
    select = Select(select_month)
    select.select_by_value('2')

    driver.find_element(By.ID, "year").send_keys("1940")

    # Wprowadź e-mail w polu rejestracji

    driver.find_element(By.ID, "login").send_keys(emails[0])

    # Kliknij przycisk "Zarejestruj się"
    time.sleep(8)
    # element = WebDriverWait(driver, 10).until(
    #    EC.element_to_be_clickable((By.XPATH, '//button[text()="Dalej"]'))
    # )
    # while not driver.find_element(By.XPATH, '//button[text()="Dalej"]').():
    # print("czkamsd")
    # time.sleep(1)
    """ while True:
        is_clicable = False
        try:
            driver.find_element(By.XPATH, '//button[text()="Dalej"]').click()
            is_clicable = True
        except WebDriverException:
            print("Element is not clickable")
        if is_clicable:
            break """

    # driver.find_element(
    #    By.CSS_SELECTOR, "sc-bcXHqe Buttons__Button-sc-g2fyk2-0 iGblCX gwugjh").click()

    # Sprawdź, czy pojawi się informacja o błędzie rejestracji lub o dostępności adresu e-mail
    # error_message = driver.find_element(
    # By.XPATH, '//div[text()="Podany login jest już zajęty"')
    # driver.find_element(By.XPATH, "//*[text()='Podany login jest już zajęty']")
    # driver.find_element(
    #    By.CLASS_NAME, "sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV")
    time.sleep(8)
    x = driver.find_element(
        By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']")
    print(x.tag_name)
    print(x.text)

    for email in emails[1:]:
        print(f"wstawiamy: {email}")
        driver.find_element(By.ID, "login").send_keys("")
        driver.find_element(By.ID, "login").clear()
        driver.find_element(By.ID, "login").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.ID, "login").send_keys(Keys.DELETE)
        #driver.refresh(By.ID, "login")
        # WebDriverWait(driver, 10).until(
        #    EC.text_to_be_present_in_element_value((By.ID, "login"), ""))
        #print("czekamy na wyczyszczenie loginu ")
        # WebDriverWait(driver, 10).until(
        #    EC.staleness_of(driver.find_element(By.ID, "login")))
        print(f'login:{driver.find_element(By.ID, "login").text}')

        #.sleep(random.randint(1, 3))
        driver.find_element(By.ID, "login").send_keys(email)
        #print(f'login:{driver.find_element(By.ID, "login").text}')
        #time.sleep(1)
        time.sleep(random.randint(1,2))
        #WebDriverWait(driver, 3).until(
        #EC.presence_of_element_located((By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']"),"Podany login jest już zajęty"))
        x = driver.find_element(
            By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']")
        # print(x)
        if x.text == "Podany login jest już zajęty":
            with open('C:\\tmp\\new_new_new_ready1000.txt', 'a') as file:
                file.write(f"{email}")  
        # print(x.text)

    # if "nie istnieje" in error_message.text:
    #    return False  # Adres e-mail nie istnieje
    # else:
    #    return True  # Adres e-mail istnieje


print("asdasd")
print(len(sys.argv))
path=sys.argv[1]
#print("sdaasd")
print(path)
with open(path, 'r',encoding='utf-8') as file:
    email_to_check = file.readlines()
    register_and_check_email_availability(email_to_check)
print(path)
