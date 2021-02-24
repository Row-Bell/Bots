#import webdriver from the selenium lib
from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        #go to tinder.com
        self.driver.get('https://tinder.com')
        
        sleep(0.5)
        #Find and click on the login
        login_btn = self.driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        login_btn.click()
        
        sleep(0.5)
        #Find and click on facebook login
        fb_btn = self.driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()
        
bot = TinderBot()
bot.login()