import logging
import time

from surebet.loading.posit import *
from surebet.loading.selenium import Selenium
from surebet.tests.loading import check_result


def test_loading():
    selenium = Selenium()

    print("loaded")

    try_load(load, name, browser=selenium.browser)
    for i in range(4):
        print("load events: ({})".format(i))

        result = try_load(load_events, name, browser=selenium.browser)
        check_result(result)

        time.sleep(1)

    selenium.quit()

    logging.info("PASS: loading")
