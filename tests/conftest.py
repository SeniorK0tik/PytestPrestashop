import random
import time
from datetime import datetime

import pytest
import requests
from pydantic import SecretStr
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from configuration.structions import User, SocialTitle
from configuration.ui import UIConfig, get_ui_config
from models.db.mysql_db import connect_db, PrestaMySQL
from models.webdriver.driver.page import Page
from models.webdriver.event_listener.listener import CustomListener
from utils.logger_loguru.logger import logger


def pytest_configure():
    url = get_ui_config().base_url

    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=15)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    response = session.get(url)
    if response.status_code != 200:
        logger.info('----------------PRESTA SERVER IS NOT AVAILABLE-----------------')
        logger.info(f'----------------STATUS CODE: {response.status_code}-----------------')
        logger.info(f'----------------RESTART IN 10 sec-----------------')
        time.sleep(10)
        pytest_configure()
    logger.info('----------------PRESTA SERVER IS AVAILABLE-----------------')


@pytest.fixture(scope='function', autouse=True)
def faker_seed():
    return random.randint(1, 100)


@pytest.fixture(scope='session')
def ui_config() -> UIConfig:
    return get_ui_config()


@pytest.fixture(scope='session', params=get_ui_config().remote_browsers.browsers)
def ui_remote(request, ui_config: UIConfig):
    ui_config.driver.capabilities = request.param
    yield ui_config


@pytest.fixture(scope='session')
def db_config(ui_config: UIConfig) -> PrestaMySQL:
    connection = connect_db(
        host=ui_config.db.host,
        port=ui_config.db.port,
        user=ui_config.db.user,
        password=ui_config.db.password,
        database=ui_config.db.db_name
    )
    return PrestaMySQL(connection)


@pytest.fixture(scope='session')
def page(ui_remote: UIConfig) -> Page:
    page_client = Page(ui_remote, CustomListener())

    page_client.wait_until_stable()
    yield page_client

    page_client.quit()


@pytest.fixture(scope='class')
def user_data(request: pytest.FixtureRequest, ui_config: UIConfig):
    new_user = User(
        social_title=SocialTitle.MR,
        first_name='Kotik',
        last_name='Usach',
        email=ui_config.presta.d_u_email,
        password=SecretStr(ui_config.presta.d_u_password),
        birthday=datetime(1995, 4, 24)
    )

    request.cls.user = new_user


def pytest_generate_tests(metafunc):
    if "user_data_comb" in metafunc.fixturenames:
        metafunc.parametrize(
            "user_data_comb",
            [("c_email", "i_password"), ("i_email", "c_password")],
            indirect=True
        )
    elif "user_data_comb_with_empty_field" in metafunc.fixturenames:
        metafunc.parametrize(
            "user_data_comb_with_empty_field",
            [("c_email", "empty_password"), ("empty_email", "c_password")],
            indirect=True
        )
