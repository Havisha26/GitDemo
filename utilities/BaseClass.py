import inspect
import logging

import pytest
#import pytest_html
#from item import item

from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logfile = logging.FileHandler('logfile.log')
        logFormatter = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s')
        logfile.setFormatter(logFormatter)
        logger.addHandler(logfile)
        logger.setLevel(logging.DEBUG)
        return logger

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)