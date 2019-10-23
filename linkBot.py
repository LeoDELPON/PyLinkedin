import time
import re
import os
import random
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException


class LinkBot:
    def __init__(self, driver):
        self.driver = driver

    def signIn(self, username, password):
        self.driver.maximize_window()
        self.driver.get(
            "https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&fromSignIn=true&trk=uno-reg-join-sign-in")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'username'))
            )
            self.driver.find_element_by_xpath(
                '//*[@id="username"]').send_keys(username)
            self.driver.find_element_by_xpath(
                '//*[@id="password"]').send_keys(password)
            self.driver.find_element_by_xpath(
                '/html/body/div/main/div/form/div[3]/button').click()
            # idon't know why but thanks to that it Bypass the captcha
            time.sleep(random.randint(50, 55))
        except(NoAlertPresentException, TimeoutException) as py_ex:
            print("[-] Form input not loaded yet! Should increase the Wait")
            print(py_ex)
            print(py_ex.args)

    def addContact(self):
        print("[+] Don't worry, your login is stacked in variable so I can't access to them :) Léo Delpon")
        username = input("[+] Give me your mail address for Linkedin: ")
        password = input("[+] Give me your password for Linkedin: ")
        nbs_of_invited_personn = int(
            input("[+] Give me the number of personn you want to add: "))

        self.signIn(username, password)
        self.driver.get("https://www.linkedin.com/mynetwork/")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'ember157'))
            )
            for i in range(1, 9):
                self.driver.find_element_by_xpath(
                    '/html/body/div[6]/div[5]/div[3]/div/div/div/div/div/div/ul/li/ul/li['+str(i)+']/div/section/div[2]/footer/button').click()
            WebDriverWait(self.driver, 1)
            for j in range(1, nbs_of_invited_personn + 1):
                time.sleep(0.5)
                self.driver.find_element_by_xpath(
                    f'/html/body/div[6]/div[5]/div[3]/div/div/div/div/div/div/div[2]/section/section/artdeco-tabs/artdeco-tabpanel[1]/ul/li[{j}]/div/section/div[2]/footer/button').click()
        except(NoAlertPresentException, TimeoutException) as py_ex:
            print("[-] 'ul' balise is not found")
            print(py_ex)
            print(py_ex.args)

    def specifiedContact(self):
        print(
            "[+] Don't worry, your login is stacked in variable so I can't access to them :) Léo Delpon")
        username = input("[+] Give me your mail address for Linkedin: ")
        password = input("[+] Give me your password for Linkedin: ")
        nbs_of_invited_personn = int(
            input("[+] Give me the number of personn you want to add: "))
        company = input("[+] Give me the name of your targeted company: ")
        message = input("[+] Give me a personnalized message: ")

        self.signIn(username, password)

        try:
            if (' ' in company) == True:
                company = re.sub(r'\s+', '-', company)
            self.driver.get(
                f"https://www.linkedin.com/company/{company}/people/")
            action = ActionChains(self.driver)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
                By.XPATH, '/html/body/div[6]/div[5]/div[3]/div/div[2]/div/main/div[2]/ul'))
            )
            action.move_to_element(self.driver.find_element_by_xpath(
                '/html/body/div[6]/div[5]/div[3]/div/div[2]/div/main/div[2]/ul'))
            action.perform()
            for k in range(1, nbs_of_invited_personn + 1):
                try:
                    time.sleep(random.randint(1, 3))
                    self.driver.find_element_by_xpath(
                        f'/html/body/div[6]/div[5]/div[3]/div/div[2]/div/main/div[2]/ul/li[{k}]/div/section/footer/button').click()
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
                        By.XPATH, '/html/body/div[4]/div/div/div[3]/button[1]'))
                    )
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[3]/button[1]').click()
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/div[1]/textarea').send_keys(message)
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[3]/button[2]').click()
                except NoSuchElementException:
                    pass
                    print("Next Target...")
        except(NoAlertPresentException, TimeoutException) as py_ex:
            print(py_ex)
            print(py_ex.args)

    def feedLiking(self):
        print(
            "[+] Don't worry, your login is stacked in variable so I can't access to them :) Léo Delpon")
        username = input("[+] Give me your mail address for Linkedin: ")
        password = input("[+] Give me your password for Linkedin: ")
        nbs_of_like = int(
            input("[+] Give me the number of publication you want to like: "))

        self.signIn(username, password)

        self.driver.get("https://www.linkedin.com/feed/")
        action = ActionChains(self.driver)
        try:
            for l in range(4, nbs_of_like + 1):
                for m in range(4, 8):
                    try:
                        action.move_to_element(self.driver.find_element_by_xpath(
                            f'/html/body/div[{m}]/div[6]/div[3]/div/div/div/div/div[2]/div[{l}]')).perform()
                    except NoSuchElementException:
                        pass
                    for n in range(4, 8):
                        try:
                            self.driver.find_element_by_xpath(
                                f'/html/body/div[{m}]/div[6]/div[3]/div/div/div/div/div[2]/div[{l}]/div/div/div[{n}]/div/div[2]/span[1]/button[1]').click()
                        except NoSuchElementException:
                            pass
        except(NoAlertPresentException, TimeoutException) as py_ex:
            print("[-] 'ul' balise is not found")
            print(py_ex)
            print(py_ex.args)

    def jobLooking(self):
        print(
            "[+] Don't worry, your login is stacked in variable so I can't access to them :) Léo Delpon")
        username = input("[+] Give me your mail address for Linkedin: ")
        password = input("[+] Give me your password for Linkedin: ")
        nbs_try = int(
            input("[+] Give me the number of personn you want to add: "))
        phone_number = input("[+] Give me your phone number please ;): ")
        job = input("[+] Give the name of you profession domain: ")
        exp = int(input("[+] Are u looking for an internship? if yes Tap 1: "))

        self.signIn(username, password)

        self.driver.get("https://www.linkedin.com/jobs/")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, '/html/body/div[6]/div[6]/div[3]/div/div[1]/section/div[2]/div[1]/div/div[2]/div/div/input'))
        ).send_keys(job, Keys.ENTER)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, '/html/body/div[6]/div[6]/div[3]/section[1]/header/div/div/div[3]/div/div/ul/li[4]/form/button'))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f'/html/body/div[6]/div[6]/div[3]/section[1]/header/div/div/div[3]/div/div/ul/li[4]/form/div/fieldset/div/ul/li[{exp}]'))).click()
        self.driver.find_element_by_xpath(
            '/html/body/div[6]/div[6]/div[3]/section[1]/header/div/div/div[3]/div/div/ul/li[4]/form/div/fieldset/div/div/div/button[2]').click()

        action = ActionChains(self.driver)
        for j in range(1, nbs_try + 1):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, f'/html/body/div[6]/div[6]/div[3]/section[1]/div[2]/div/div/div[1]/div[2]/div/ul/li[{j}]/div')))
            action.move_to_element(self.driver.find_element_by_xpath(
                f'/html/body/div[6]/div[6]/div[3]/section[1]/div[2]/div/div/div[1]/div[2]/div/ul/li[{j}]/div')).perform()
            time.sleep(random.randint(1, 3))
            self.driver.find_element_by_xpath(
                f'/html/body/div[6]/div[6]/div[3]/section[1]/div[2]/div/div/div[1]/div[2]/div/ul/li[{j}]/div').click()
            try:
                if self.driver.find_element_by_xpath('/html/body/div[6]/div[6]/div[3]/section[1]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div/button/span').text == "Candidature simplifiée":
                    time.sleep(random.randint(1, 2))
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
                        By.XPATH, '/html/body/div[6]/div[6]/div[3]/section[1]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div/button'))).click()
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/form/div/div[1]/input'))).send_keys(phone_number)
                    self.driver.find_element_by_id(
                        'file-browse-input').send_keys(os.getcwd()+"/CVWeb.pdf")
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button[2]').click()
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[4]/div/div/button')))
                    time.sleep(random.randint(1, 2))
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/button').click()
                elif self.driver.find_element_by_xpath('/html/body/div[6]/div[6]/div[3]/section[1]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div/button/span').text == "Postuler":
                    print("Next Target...")
                    pass
            except (NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementClickInterceptedException):
                pass
