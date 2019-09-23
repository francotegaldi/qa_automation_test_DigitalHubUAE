import pytest
from selenium import webdriver
import json
import time

@pytest.yield_fixture(scope='class')
def first_challenge_setup(request):

    time.sleep(10)

    _hub_url = 'http://localhost:4444/wd/hub'
    _base_url = 'https://trello.com'

    caps = {'browserName': 'chrome',"goog:chromeOptions": {"args":[ "--headless", "--disable-gpu", "--no-sandbox"]}}
    driver = webdriver.Remote(
        command_executor='http://chrome:4444/wd/hub',
        desired_capabilities=caps
    )

    driver.get(_base_url)
    driver.implicitly_wait(10)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()

@pytest.yield_fixture(scope='class')
def second_challenge_setup(request):

    with open("/src/utils/data.json") as jsonfile:
        data = json.load(jsonfile)

    if request.cls is not None:
        request.cls.data = data

    yield data

