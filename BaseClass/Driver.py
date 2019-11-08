from appium import webdriver

global driver
def launchApp():
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0"
        desired_caps["deviceName"] = "qwerty"
        desired_caps["appPackage"] = "com.example.android.apis"
        desired_caps["appActivity"] = "com.example.android.apis.ApiDemos"
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(2)
        return driver


