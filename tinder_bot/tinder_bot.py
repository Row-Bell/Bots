#import webdriver from the selenium lib
from selenium import webdriver
from time import sleep
from secret import email, password

class TinderBot():
    #Initiate the bot
    def __init__(self):
        self.driver = webdriver.Chrome()
     
    #Logging into Tinder
    def login(self):
        #go to tinder.com
        self.driver.get('https://tinder.com')
        sleep(1)
        
        privacy_accept = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        privacy_accept.click()
        
        sleep(1)
        #Find and click on the login
        login_btn = self.driver.find_element_by_xpath('//*[@id="t-1801132545"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        login_btn.click()
        
        sleep(1.5)
        #Find and click on facebook login
        fb_btn = self.driver.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()
        
        #Setting the base window and pop-up window variables        
        base_window = self.driver.window_handles[0]
        popup_window = self.driver.window_handles[1]
        
        #switching focus to the pop-up login window
        self.driver.switch_to_window(popup_window)
        
        #Settup email and password
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)
        
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)
        
        sleep(1)
        #Click on the login button with FULL XPATH
        popup_login = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        popup_login.click()
        
                
        #switching focus from the pop-up login window back to the basewindow
        self.driver.switch_to_window(base_window)
        
        sleep(3)
        popup_1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        
        sleep(1)
        popup_2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        

    
    #Swipe right!
    def like(self):
        swipe_right= self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div[1]/div[2]/div[4]/button')
        sleep(2)
        swipe_right.click()  
    #Swipe left!
    def dislike(self):
        swipe_left = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div[1]/div[2]/div[2]/button')
        swipe_left.click()
        
    def autoswipe(self):
        while True:
            sleep(0.5)
            self.dislike()
        
bot = TinderBot()
bot.login()


