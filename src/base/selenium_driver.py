from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'link':
            return By.LINK_TEXT
        else:
            print("Locator not supported")

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element found: " + locator)
        except:
            print("Element not found: " + locator)
        return element

    def clickElement(self, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on element with locator: " + locator)
        except:
            print("Could not click on element with locator: " + locator)

    def dobleClickElement(self, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            element.dobleClickElement()
            print("Clicked on element with locator: " + locator)
        except:
            print("Could not click on element with locator: " + locator)

    def getElementText(self, locator, locatorType='id'):
        try:
            _element = self.getElement(locator, locatorType)
            _element_text = _element.text
            print('Text: "' + _element_text + '" from element with locator: ' + locator)
            return _element_text
        except:
            print("Could not get text from element with locator: " + locator)

    def getElementValue(self, locator, locatorType='id'):
        try:
            _element = self.getElement(locator, locatorType)
            _element_value = _element.get_attribute("value")

            print('Element value: "' + _element_value + '" from element with locator: ' + locator)
            return _element_value
        except:
            print("Could not get value from element with locator: " + locator)

    def clearElementValue(self, locator, locatorType='id'):
        _element = self.getElement(locator, locatorType)
        _element.clear()

    def sendKeys(self, locator, locatorType, keys):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(keys)
            print('Sent: "' + str(keys) + '" to element with locator: ' + locator)
        except:
            print('Could not send: "' + str(keys) + '" to element with locator: ' + locator)

    def isElementPresent(self, locator, locatorType):
        element = self.getElement(locator, locatorType)
        try:
            if element is not None:
                # print("Element found: " + locator)
                return True
            else:
                # print("Element not found: " + locator)
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType='id', timeout=20, pollFrequency=0.5):
        print("Waiting for element: " + str(locator))
        wait = WebDriverWait(self.driver, timeout, pollFrequency, ignored_exceptions=[NoSuchElementException,
                                                                                   ElementNotVisibleException,
                                                                                   ElementNotVisibleException,
                                                                                   ElementNotSelectableException])
        element = wait.until(EC.presence_of_element_located((self.getByType(locatorType), locator)))
        return element

    def goToiFrame(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            self.driver.switch_to.frame(element)
            print("Switching to iFrame with locator: " + locator)
        except:
            print("Could not switch to iFrame with locator: " + locator)

    def getMultipleElements(self, locator, locatorType):
        try:
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            print("Found element list with locator " + locator + ". List contains " + str(len(elementList)) + " elements")
        except:
            print("Element list not found: " + locator)
        return elementList

    def clickElementFromList(self, locator, locatorType, index):
        try:
            elements = self.getMultipleElements(locator, locatorType)
            elements[index].click()
            print("Clicked on element with locator " + locator + ", on index " + str(len(elements)))
        except:
            print("Could not click on element with locator " + locator + ", on index " + str(len(elements)))

    def verifyIsEnabled(self, locator, locatorType):
        element = self.getElement(locator, locatorType)
        return element.is_enabled()

    def generate_list_of_elements_text(self, locator, locatorType):
        elements = self.getMultipleElements(locator, locatorType)
        elementsText = []
        for element in elements:
            elementsText.append(element.text)
        print(f'Generated list of elements\' text: (locator: {locator})\n{elementsText}' )
        return elementsText

