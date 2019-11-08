import pytest
from BusinessLogic.AnimationsBL import AnimationBL
from BaseClass import Driver

@pytest.mark.priority1
def test_app_launch():
    Driver.launchApp()

@pytest.mark.priority2
def test_animation():
    AnBl = AnimationBL()
    AnBl.selectbutton()
    AnBl.showAnimation()

@pytest.mark.priority3
def test_hide():
    AnBl = AnimationBL()
    AnBl.hide()
    AnBl.zerobttn()
    condition = AnBl.zerobttn()
    assert condition==False, "Hide functionality is not working"
    AnBl.firstbttn()
    AnBl.secondbttn()
    AnBl.thirdbttn()

@pytest.mark.priority4
def test_show():
    AnBl = AnimationBL()
    AnBl.showbttn()




