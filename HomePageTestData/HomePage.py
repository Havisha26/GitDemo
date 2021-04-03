from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    name = (By.CSS_SELECTOR,"[name='name']")
    email = (By.CSS_SELECTOR,"[name='email']")
    pwd = (By.CSS_SELECTOR,"[type='password']")
    chckbox = (By.ID,"exampleCheck1")
    gender = (By.ID,"exampleFormControlSelect1")
    prof = (By.CSS_SELECTOR,"[id='inlineRadio2']")
    bday = (By.CSS_SELECTOR,"[name='bday']")
    submit = (By.CLASS_NAME,"btn-success")
    scsMsg = (By.CLASS_NAME,"alert-dismissible")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEMail(self):
        return self.driver.find_element(*HomePage.email)

    def getPwd(self):
        return self.driver.find_element(*HomePage.pwd)

    def getChckBox(self):
        return self.driver.find_element(*HomePage.chckbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getProf(self):
        return self.driver.find_element(*HomePage.prof)

    def getBDay(self):
        return self.driver.find_element(*HomePage.bday)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def ScsMsg(self):
        return self.driver.find_element(*HomePage.scsMsg)