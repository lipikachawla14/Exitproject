from DataSource import DataReader
from BaseClass import Driver
import time

class AnimationPL:
    read = DataReader.DataReader()
    def select_animationBtn(self):
        return Driver.driver.find_element_by_xpath(self.read.reader("animation"))

    def hide_showanimation(self):
        return Driver.driver.find_element_by_xpath(self.read.reader("show_animations"))

    def hide(self):
        return Driver.driver.find_element_by_xpath(self.read.reader("hide_checkbox"))

    def selectzero(self):
        try:
            return Driver.driver.find_element_by_xpath(self.read.reader("zero_button"))
        except:
            print('an excpetion occurs')
    def selectfirst(self):
        return Driver.driver.find_element_by_xpath(self.read.reader("first_button"))

    def selectsecond(self):
        return Driver.driver.find_element_by_xpath(self.read.reader("second_button"))

    def selectthird(self):
        return Driver.driver.find_element_by_xpath(self.read.reader("third_button"))

    def selectshow(self):
        return Driver.driver.find_element_by_xpath(self.read.reader("show_button"))




