# Any Pytest fileand pytest method name should start with test_ keyword
# -k is used to rn specific keyword test case.
# to run from cmd, use py.test keyword
# use @pytest.mark with required tags to run  specific type test cases. ex: @pytest.mark.smoke,
# @pytest.mark.skip to skip a TC,
# @pytest.mark.xfail executes a TC but doesn't display fail or pass reports of that TC in the output


import pytest

#from pytestsDemo.HomePageTestData.HomePage import HomePage
#from pytestsDemo.HomePageTestData.HomePageData import HomePageTestData
#from pytestsDemo.utilities.BaseClass import BaseClass

from HomePageTestData.HomePage import HomePage
from HomePageTestData.HomePageData import HomePageTestData
from utilities.BaseClass import BaseClass


class TestDemo(BaseClass):

    def test_demo1(self,getData):
        log = self.getLogger()
        hmPg = HomePage(self.driver)
        hmPg.getName().send_keys(getData["Firstname"])
        hmPg.getEMail().send_keys(getData["Lastname"])
        hmPg.getEMail().send_keys(getData["email"])
        hmPg.getPwd().send_keys("Havisha$26")
        hmPg.getChckBox().click()
        self.selectOptionByText(hmPg.getGender(), getData["gender"])
        hmPg.getProf().click()
        hmPg.getBDay().send_keys("26-07-1994")
        hmPg.getSubmit().click()
        self.driver.implicitly_wait(5)
        successMsg = hmPg.ScsMsg().text
        assert "Success! The Form has been submitted successfully!." in successMsg
        self.driver.refresh()

    @pytest.fixture(params=HomePageTestData.testdata("Sno"))
    def getData(self,request):
        return request.param
