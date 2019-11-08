
from CommonUtills import CommonUtilities
from ObjectRepository import AnimationsPL

class AnimationBL:
    obj=CommonUtilities.CommonUtills()
    select=AnimationsPL.AnimationPL()

    def selectbutton(self):
        try:
            self.obj.click(self.select.select_animationBtn())
            return True
        except Exception as e:
            print(str(e))
            print('no element found')
            return False

    def showAnimation(self):
            try:
                self.obj.click(self.select.hide_showanimation())
                return True
            except:
                print('no element found')
                return False

    def hide(self):
        try:
            self.obj.click(self.select.hide())
            return True
        except Exception as e:
            print(str(e))
            print('no element found')
            return False

    def zerobttn(self):
        try:
           if self.obj.isDisplayed(self.select.selectzero()):
               self.obj.click(self.select.selectzero())
               return True
           else:
               return False
        except:
            print('no element found')
            return False

    def firstbttn(self):
        try:
            self.obj.click(self.select.selectfirst())
            return True
        except:
             print('no element found')
             return False

    def secondbttn(self):
         try:
             self.obj.click(self.select.selectsecond())
             return True
         except:
             print('no element found')
             return False

    def thirdbttn(self):
        try:
            self.obj.click(self.select.selectthird())
            return True
        except:
            print('no element found')
            return False

    def showbttn(self):
        try:
            if self.obj.isDisplayed(self.select.selectshow()):
               self.obj.click(self.select.selectshow())
               return True
        except:
            print('no element found')
            return False














