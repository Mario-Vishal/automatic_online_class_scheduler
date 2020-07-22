#!/usr/bin/python
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
import pandas as pd 
import numpy as np
import requests
from datetime import datetime
import os
import time

class automate_class:
    def __init__(self,filename):
        self.date =int(datetime.date(datetime.now()).strftime("%d"))
        self.time = int(datetime.time(datetime.now()).strftime("%H"))
        self.browser=None
        self.link=None
        self.filename = filename

    def connect_driver(self):
        try:
            opt= Options()
            opt.add_experimental_option("prefs",{
               "profile.default_content_setting_values.media_stream_mic": 1,
                "profile.default_content_setting_values.notifications": 1,
            })
            driver_path =os.getcwd()+"/chromedriver"
            self.browser = webdriver.Chrome(chrome_options=opt,executable_path=driver_path)
            print("connected")
        except Exception as exp:
            print(exp)
    
    def login_account(self):
        url = 'https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.co.in%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        self.browser.get(url)
        
        email  = self.browser.find_element_by_name('identifier')
        email.send_keys("YOUR EMAIL ID FOR GOOGLE MEET")
        email.send_keys(Keys.RETURN)
        time.sleep(2)
        password = self.browser.find_element_by_name('password')
        password.send_keys('YOUR PASSWORD FOR GOOGLE MEET')
        password.send_keys(Keys.RETURN)
        
        #To open a new tab
        time.sleep(3)
        
    def validate_dates(self):
        rt = pd.read_csv(self.filename)
        feed = rt[(rt.date==self.date) & (rt.time==self.time)][['staff','links']].values
        
        if feed.size<2:
            print("Hey you have either no class or your dates are incorrect check your csv file!!!")
            return False
        else:
            print("Date exists!")
            print(f"You have a class by {feed[0,0]} ma'am")
            self.link=feed[0,1]
            return True 
        
    
    def google_meet_connect(self):
        try:
            # self.login_account()
            self.login_account()
            self.browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND+'t')
            # link = self.get_link(d,t)
            time.sleep(1.5)
            self.browser.get(self.link)
            print("Opening google meet")
            time.sleep(3)
            print("Disabling mic.........")
            print()
            #Mutting mic-----------------
            mic = self.browser.find_element_by_tag_name('body')
            mic.send_keys(Keys.CONTROL+"d")
            time.sleep(1)
            print("Disabling camera.......")
            #disabling camera-----------------
            camera = self.browser.find_element_by_tag_name('body')
            camera.send_keys(Keys.CONTROL+"e")
            time.sleep(5)
        except Exception as e:
            print(e)

    def zoom_connect(self):
        try:
            self.browser.get(self.link)
            print("Opening Zoom..")
            print()
            print("Currently selenium doesn't support opening applications from the browser!!")
            print()
            print("open your zoom app manually!.")
        except Exception as e:
            print(e)

    def detect_platform_and_connect(self):

        if self.validate_dates():

            if 'https://' not in self.link:
                self.link='https://'+self.link
        
            if "zoom" in self.link:
                # My zoom links are attached with Meeting Id and it would be invalid if paste the link directly !
                #removing Meeting id...
                self.link = re.sub('(Meeting.*)','',self.link)
                self.zoom_connect()
            elif "google" in self.link:

                self.google_meet_connect()
            else:
                self.browser.get(self.link)
                print("Link is neither zoom or google meet")
        else:

            print("exiting.....")
            self.browser.quit()
        
       
my_lec = {'saraswathi':'Ethics','gowri':'Web Programming','aarthi':'Software Quality Assurance',
          'prabhavathi':'Wireless Sensor Networks','asha':'Artificial Intelligence'}


class create_schedule:
    def __init__(self,filename):
        self.filename = self.filename
        self.columns =None

        

cl = automate_class('sch.csv')

cl.connect_driver()
cl.detect_platform_and_connect()






