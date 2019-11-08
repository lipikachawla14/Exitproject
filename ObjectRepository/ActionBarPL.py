from DataSource import DataReader
from BaseClass import Driver
import time

class ActionPL:
    call=DataReader.DataReader()
    def selectapp(self):
        return Driver.driver.find_element_by_xpath(self.call.reader("app"))

    def selectactionbar(self):
        time.sleep(2)
        return Driver.driver.find_element_by_xpath(self.call.reader("bar"))

    def selectdisplay(self):
        time.sleep(2)
        return Driver.driver.find_element_by_xpath(self.call.reader("display_option"))

    def show_Title(self):
        time.sleep(2)
        return Driver.driver.find_element_by_xpath(self.call.reader("show_titlebar"))

    def get_Title(self):
        time.sleep(2)
        try:
            return Driver.driver.find_element_by_xpath(self.call.reader("title"))
        except:
            print("an exception occurs")


