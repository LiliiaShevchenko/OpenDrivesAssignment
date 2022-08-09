import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from pages.homepage import Homepage


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver

@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    url = 'http://localhost:3000/'
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def home_page(setup):
    yield Homepage(setup)
