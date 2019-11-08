from CommonUtills import CommonUtilities
from ObjectRepository import ActionBarPL

class ActionBL:
    commons=CommonUtilities.CommonUtills()
    selects=ActionBarPL.ActionPL()

    def selectapp(self):
        try:
            self.commons.click(self.selects.selectapp())
            return True
        except:
            print('no element found')
            return False

    def selectbar(self):
        try:
            self.commons.click(self.selects.selectactionbar())
            return True
        except:
            print('no element found')
            return False

    def display(self):
        try:
            self.commons.click(self.selects.selectdisplay())
            return True
        except:
            print('n element found')
            return False

    def showTitle(self):
        try:
            if self.commons.isDisplayed(self.selects.show_Title()):
                self.commons.click(self.selects.show_Title())
                if not self.commons.isDisplayed(self.selects.get_Title()):
                    self.commons.click(self.selects.show_Title())
                    if self.commons.isDisplayed(self.selects.get_Title()):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        except :
            print('no element found')
            return False














