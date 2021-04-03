import pytest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="chrome", help="Chrome is invoked when no browser is passed"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("--cmdopt")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\user\\PycharmProjects\\chromedriver_win32 (1)\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Program Files\\geckodriver.exe")
    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path="C:\\Program Files\\Internet Explorer\\iexplore.exe")
    # driver.back() ->navigate to back pages
    # driver.forward() ->navigate to next page
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


#@pytest.fixture(scope="class")
#def setup():
    #print("Fixture would be executing at the beginning of the execution")
    #yield
    #print("Yield would be executing at the end of the execution")


#@pytest.fixture()
#def dataLoad():
    #return["data1","data2","data3"]


#@pytest.fixture(params=[("Chrome","Havisha","Vemuri"),("Firefox","Honey","Vemuri"),("IE","Name")])
#def paramLoad(request):
 #   return request.param