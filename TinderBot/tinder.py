import selenium
import pychrome
import time
from htmlObj import HTMLObj
from chattingTools import Message, Dialog
from dinamicPrint import Dprint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def strTodigits(str):
    digits = []
    for i in str:
        digits.append(i)
    return digits

class Tinder:

    def __init__(self, browser, phone, code, timeout, waitTime):
        self.browser = browser
        self.phone = phone
        self.timeout = timeout
        self.waitTime = waitTime
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.code = code

    '''     
    def click(self, xPath, waitTime=-1):
        if waitTime<0:
            waitTime = self.waitTime
        elem = self.getVis(xPath)
        elem.click()
        time.sleep(waitTime) 
    '''

    def click(self, xPath, waitTime=-1):
        if waitTime<0:
            waitTime = self.waitTime
        elem = self.getPresence(xPath)
        self.browser.execute_script('''
        arguments[0].click();
        ''', elem)
        time.sleep(waitTime)


    def sendKeys(self, xPath, keys, waitTime=-1):
        if waitTime<0:
            waitTime = self.waitTime
        elem = self.getPresence(xPath)
        elem.send_keys(keys)
        time.sleep(waitTime)


    '''     
    def sendKeys(self, xPath, keys, waitTime=-1):
        if waitTime<0:
            waitTime = self.waitTime
        elem = self.getPresence(xPath)
        self.browser.execute_script("
        arguments[0].value = arguments[1];
        ", elem, keys)
        time.sleep(self.waitTime)
    '''
    def getVis(self, xPath):
        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, xPath)))
        return elem
        
    ''' 
    def getPresence(self, xPath):
        elem = self.wait.until(EC.presence_of_element_located((By.XPATH, xPath)))
        return elem '''

    def getPresence(self, xPath):
        startT = time.time()
        curT = time.time()
        elem = None
        while not elem and curT - startT < self.timeout:
            try:
                elem = self.browser.find_element_by_xpath(xPath)
            except:
                pass
            curT = time.time()
        return elem

    def kill_promo(self):
        try:
            elem = self.browser.find_element_by_class_name("techbutton")
            elem.click()
        except:
            pass
        try:
            denyBtn = self.browser.find_element_by_xpath(
                '//*[@id="content"]/div/span/div/div[2]/div/div/div[3]/button[2]'
                )
            denyBtn.click()
        except:
            pass

    def killStartingDialogs(self):
        try:
            self.click('//*[@id="content"]/span/div/div[2]/div/div/div[3]/button[1]')
        except:
            pass
        try:
            self.click('//*[@id="content"]/span/div/div[2]/div/div/div[3]/button[1]')  
        except:
            pass    
        

    def login(self):
        print("logining, wait")
        self.browser.get("http://tinder.com/")
        time.sleep(self.waitTime*3)
        try:
            enterBtn = self.browser.find_element_by_xpath(
                '//*[@id="content"]/span/div/div/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div/button'
                )
            enterBtn.click()
        except:
            pass
        self.click('//*[@id="modal-manager"]/div/div/div[2]/div/div[3]/div[1]/button')
        time.sleep(self.waitTime*3)
        try:
            fr = self.browser.find_elements_by_tag_name("iframe")[1]
            self.browser.switch_to.frame(fr)
            #elem = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="u_0_6p"]')))
            elem = self.browser.find_element_by_xpath('//*[@id="u_0_6p"]')
        except:
            self.loginVar2()
            return
        self.browser.execute_script('''
        var elem = arguments[0];
        var value = arguments[1];
        elem.value = value;
        ''', elem, self.code)
        self.sendKeys('//*[@id="u_0_6q"]', self.phone)
        self.click('//*[@id="u_0_6r"]')
        code = input("enter code from sms:")
        self.sendKeys('//*[@id="u_0_3"]', code)
        self.click('//*[@id="u_0_4"]')
        print("logged in")
        self.killStartingDialogs()

    def loginVar2(self):
        try:
            self.sendKeys('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input',self.phone)
            self.click('//*[@id="modal-manager"]/div/div/div[2]/button')
        except:
            self.login()
            return
        code = input("enter code from sms:")
        code = strTodigits(code)
        for idx in range(0, len(code)):
            self.sendKeys(f'//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[{idx+1}]',code[idx],waitTime=0.5)
        self.click('//*[@id="modal-manager"]/div/div/div[2]/button')
        print("logged in")
        self.killStartingDialogs()

    def setEnglish(self):
        print("switching language to english")
        time.sleep(self.waitTime)
        #profileBtn = HTMLObj(self.timeout, xpath = '//*[@id="content"]/span/div/div[1]/div/aside/div/a/span/span')    
        profileBtn = HTMLObj(self.timeout, xpath = '//*[@id="content"]/span/div/div[1]/div/aside/div/a')  
        try:
            profileBtn.click(self.browser)
        except:
            raise
        time.sleep(self.waitTime)
        languageBtn = HTMLObj(
            self.timeout, 
            xpath = '//*[@id="content"]/span/div/div[1]/div/aside/nav/div/div/div/div/div/div/div[7]/div/a/div/label/div'
            )    
        try:
            languageBtn.click(self.browser)
        except:
            raise
        time.sleep(self.waitTime)
        englishBtn = HTMLObj(
            self.timeout, 
            xpath = '//*[@id="content"]/span/div/div[1]/div/aside/nav/div/div/div/div/div/div/div/div[1]/label/div'
            )    
        try:
            englishBtn.click(self.browser)
        except:
            raise
        time.sleep(self.waitTime)
        exitBtn = HTMLObj(self.timeout, xpath = '//*[@id="content"]/span/div/div[1]/div/aside/div/div/a')    
        try:
            exitBtn.click(self.browser)
        except:
            raise
        time.sleep(self.waitTime)
        exitBtn = HTMLObj(self.timeout, xpath = '//*[@id="content"]/span/div/div[1]/div/aside/div/div/a')    
        try:
            exitBtn.click(self.browser)
        except:
            raise
        time.sleep(self.waitTime)

    def like(self):
        time.sleep(2)
        counter = 0
        stop = False
        dp = Dprint()
        dp.pulse()
        while True:
            clicked = True
            try:
                self.click(
                    '//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]', 
                    waitTime=self.waitTime/10
                    )
            except:
                clicked = False
            time.sleep(self.waitTime)
            try:
                continueBtn = self.browser.find_element_by_xpath(
                    '//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div/button'
                    )
                continueBtn.click()
            except:
                pass
            try:
                stopElem = self.browser.find_element_by_xpath(
                    '//*[@id="modal-manager"]/div/div/div[1]/div[2]/div[1]/div/div[1]/div/button/span/div/h3/span'
                    )
                if stopElem.text == "You're Out of Likes!":
                    stop = True
            except:
                pass
            try:
                denyBtn =  self.browser.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
                denyBtn.click()
            except:
                pass
            if stop:
                break
            else:
                if clicked:
                    counter += 1
                dp.print(f"made {counter} likes")
        dp.end()
        print(f"made {counter} likes")

    def spam(self, pattern):
        time.sleep(self.waitTime)
        toPairsLink = self.browser.find_element_by_xpath(
            '//*[@id="content"]/span/div/div[1]/div/aside/nav/div/div/div/div[1]/div/div[1]'
            )
        toPairsLink.click()
        self.kill_promo()
        links =  self.browser.find_elements_by_class_name("matchListItem")
        counter = 0
        dp = Dprint()

        while len(links)>1:
            link = links[1]
            dialog = Dialog()
            time.sleep(self.waitTime)
            self.kill_promo()
            link.click()
            time.sleep(self.waitTime)
            reply = dialog.getReply(pattern)
            if reply:
                try:
                    '''
                    editor = self.browser.find_element_by_xpath(
                        '//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/form/textarea'
                        )
                    '''
                    editor = self.browser.find_element_by_xpath(
                        '//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[2]/form/textarea'
                        )                    
                    editor.send_keys(reply)
                    sendBtn = self.browser.find_element_by_xpath(
                        '//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[2]/form/button'
                        )
                    sendBtn.click()
                    time.sleep(self.waitTime)
                except:
                    pass
            
            closeBtn = self.browser.find_element_by_xpath(
                '//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/nav/a/div'
                )
            closeBtn.click()
            time.sleep(self.waitTime)
            toPairsLink = self.browser.find_element_by_xpath(
                '//*[@id="content"]/span/div/div[1]/div/aside/nav/div/div/div/div[1]/div/div[1]'
                )
            toPairsLink.click()
            time.sleep(self.waitTime)
            links =  self.browser.find_elements_by_class_name("matchListItem")
            counter += 1
            dp.print(f"found {counter} new contacts")
            links =  self.browser.find_elements_by_class_name("matchListItem")
        dp.end()
        print(f"found {counter} new contacts")

    def parseDialogs(self, pattern):
        '''     toDialogsLink = self.browser.find_element_by_xpath(
            '//*[@id="content"]/span/div/div[1]/div/aside/nav/div/div/div/div[1]/div/div[2]'
            )
        toDialogsLink.click()
        time.sleep(self.waitTime) '''
        print("Parsing dialogs, press ctrl+c to interrupt")
        dp = Dprint()
        dp.pulse()

        while True:
            steps = 30
            step = 0
            self.browser.refresh()
            time.sleep(self.waitTime)
            toDialogsLink = self.browser.find_element_by_xpath(
                '//*[@id="content"]/span/div/div[1]/div/aside/nav/div/div/div/div[1]/div/div[2]'
                )
            toDialogsLink.click()
            time.sleep(self.waitTime)
            links = self.browser.find_elements_by_class_name('messageListItem__name')
            length = len(links)
            while step<steps:
                for i in range(steps):
                    print((i, length))
                    try:
                        links = self.browser.find_elements_by_class_name('messageListItem__name')
                        link = links[i]
                        link.click()
                        step += 1
                    except:
                        next
                    time.sleep(self.waitTime)
                    dialog = Dialog()
                    messDivs = self.browser.find_elements_by_class_name('msg')
                    messDivs = list(filter(lambda x:"BreakWord" in x.get_attribute("class"),messDivs))
                    for messDiv in messDivs:
                        messTxt = messDiv.text
                        if "C(#fff)" in messDiv.get_attribute("class"):
                            messDir = Message.OUT
                        else:
                            messDir = Message.IN
                        message = Message(messDir,messTxt)
                        dialog.addMessage(message)
                    reply = dialog.getReply(pattern)
                    if reply:
                        for mess in reply:
                            try:
                                '''
                                editor = self.browser.find_element_by_xpath(
                                    '//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/form/textarea'
                                    )
                                '''
                                editor = self.browser.find_element_by_xpath(
                                    '//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[2]/form/textarea'
                                    )    
                                editor.send_keys(mess)
                                '''
                                sendBtn = self.browser.find_element_by_xpath(
                                    '//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/form/button'
                                    )
                                '''
                                sendBtn = self.browser.find_element_by_xpath(
                                    '//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[2]/form/button'
                                    )
                                sendBtn.click()
                            except:
                                pass    
