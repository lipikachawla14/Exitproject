import pytest
from BusinessLogic.ActionBarBL import ActionBL
from BaseClass import Driver

@pytest.mark.priority1
def test_launch():
    Driver.launchApp()

@pytest.mark.priority2
def test_actionbar():
    AcBl = ActionBL()
    AcBl.selectapp()
    AcBl.selectbar()

@pytest.mark.priority3
def test_actions():
    AcBl = ActionBL()
    AcBl.display()

@pytest.mark.priority4
def test_showTitle():
    AcBl = ActionBL()
    AcBl.showTitle()
    check = AcBl.showTitle()
    assert check==True,"Title is not visible"

