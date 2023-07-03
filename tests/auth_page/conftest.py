import pytest

from configuration.ui import UIConfig
from models.webdriver.driver.page import Page
from page_objects.login_page import LoginPage


@pytest.fixture(scope='function')
def user_data_comb(user_data, request, faker):
    if request.param == ("c_email", "i_password"):
        return (request.cls.user.email, faker.password())
    elif request.param == ("i_email", "c_password"):
        return (faker.email(), request.cls.user.password)
    else:
        raise ValueError("invalid internal test config")


@pytest.fixture(scope='function')
def user_data_comb_with_empty_field(user_data, request):
    if request.param == ("c_email", "empty_password"):
        return (request.cls.user.email, '')
    elif request.param == ("empty_email", "c_password"):
        return ('', request.cls.user.password)
    else:
        raise ValueError("invalid internal test config")


@pytest.fixture(scope="function")
def try_login_page(page: Page, ui_config: UIConfig):
    new_page = LoginPage(page=page)
    new_page.visit(ui_config.base_url + 'login')
    yield new_page
    new_page.delete_all_cookies()
