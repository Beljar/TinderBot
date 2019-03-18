import selenium
import pychrome
import requests, os, bs4
from chattingTools import Pattern
from tinder import Tinder
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyfiglet import Figlet

def readSettings(path):
    settings ={}
    with open(path) as f:
        reader = csv.reader(f, delimiter = ":", quotechar = '"')
        for row in reader:
            settings[row[0]]=row[1]
    return settings

def main():
    f = Figlet(font='slant')
    print (f.renderText('==TinderBot=='))
    SETTINGSPATH = "TinderBot\\settings.csv"
    PATTERNPATH = "TinderBot\\spamScript.csv"
    settings = readSettings(SETTINGSPATH)
    pattern = Pattern()
    pattern.importFromCSV(PATTERNPATH)
    phone = settings["phone"]
    code = settings["code"]
    headless = int(settings["headless"])
    timeout = float(settings["timeout"])
    waitTime = float(settings["waitTime"])
    webdriverPath = settings["webdriverPath"]
    chrome_options = webdriver.ChromeOptions()
    firefox_options = webdriver.FirefoxOptions()
    chrome_options.add_argument('log-level=3')
    if headless:
        chrome_options.add_argument('headless')
        chrome_options.add_argument('remote-debugging-port=9222')
    #firefox_options.add_argument('-headless')
    #firefox_options.add_argument('--start-debugger-server')
    chrome_options.add_argument('window-size=1600x1200')
    prefs = {"profile.default_content_setting_values.notifications" : 2,'profile.managed_default_content_settings.images':2}
    chrome_options.add_experimental_option("prefs",prefs)
    #prefs = {'profile.managed_default_content_settings.images':2}
    #chromeOptions.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(webdriverPath,chrome_options=chrome_options)
    #browser = webdriver.Firefox(firefox_options=firefox_options)
    browser.set_window_size(1600, 1200)
    tinder = Tinder(browser, phone, code, timeout, waitTime)
    browser.get("https://tinder.com/")
    tinder.login()
    #input("Press enter, when logged in")
    tinder.setEnglish()
    tinder.like()
    tinder.spam(pattern)
    tinder.parseDialogs(pattern)

if __name__ == "__main__":
    main()    