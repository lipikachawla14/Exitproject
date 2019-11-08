

class CommonUtills:
    def click(self,button):
        if button is not None:
            button.click()
            return True
        else:
            print('button not found')
            return False

    def isDisplayed(self,element):
        if element is not None:
            t=element.is_displayed()
            return t
        else:
            print('no such element found')
            return False