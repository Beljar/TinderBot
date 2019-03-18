import time
from dinamicPrint import Dprint

class HTMLObj:

    def __init__(self,timeout,id=None,CSSclass=None,name=None,xpath=None):
        self.id=id
        self.CSSclass=CSSclass
        self.name=name
        self.xpath=xpath
        self.timeout=timeout

    def getElem(self,browser):
        start = time.time()
        cur = start
        elem=None
        dp = Dprint()
        dp.pulse()
        while cur-start<self.timeout and not elem:
            try:
                if self.id:
                    elem = browser.find_element_by_id(self.id)
                elif self.name:
                    elem = browser.find_element_by_name(self.name)
                elif self.CSSclass:
                    elem = browser.find_elements_by_class_name(self.CSSclass)
                elif self.xpath:
                    elem = browser.find_element_by_xpath(self.xpath)
            except:
                pass
            cur = time.time()
        dp.end()
        return elem
        
    def click(self, browser):
        elem = self.getElem(browser)
        try:
            elem.click()
        except Exception as error:
            #print(f"Couldn't click: {repr(error)}")
            raise