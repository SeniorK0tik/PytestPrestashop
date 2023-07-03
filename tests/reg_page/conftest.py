import allure
import pytest

from configuration.structions import User
from configuration.ui import UIConfig
from models.db.mysql_db import PrestaMySQL
from models.webdriver.driver.page import Page
from page_objects.registration_page import RegistrationPage


@pytest.fixture(scope='function')
def random_user(request: pytest.FixtureRequest, db_config: PrestaMySQL):
    new_user = User.get_random()
    request.cls.user = new_user
    allure.dynamic.description("User: {}".format(new_user))

    def delete_user():
        db_config.delete_user(new_user.email)
    request.addfinalizer(delete_user)


@pytest.fixture(scope="function")
def try_reg_page(page: Page, ui_config: UIConfig):
    new_page = RegistrationPage(page=page)
    new_page.visit(ui_config.base_url + 'login?create_account')
    yield new_page
    new_page.delete_all_cookies()
