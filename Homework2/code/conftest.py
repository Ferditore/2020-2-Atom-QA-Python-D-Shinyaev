from ui.fixtures import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

CAPABILITIES = {'browserName': 'chrome', 'version': '80.0', 'platform': 'LINUX'}


def pytest_addoption(parser):
    parser.addoption('--selenoid', default='none')


@pytest.fixture(scope='session')
def config(request):
    selenoid = request.config.getoption('--selenoid')

    return {'selenoid': selenoid}


@pytest.fixture(scope='function')
def driver(config):
    if config['selenoid'] == 'none':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        host, port = config['selenoid'].split(':')
        driver = webdriver.Remote(command_executor=f'http://{host}:{port}/wd/hub',
                                  desired_capabilities=CAPABILITIES)
    driver.maximize_window()
    yield driver
    driver.quit()
