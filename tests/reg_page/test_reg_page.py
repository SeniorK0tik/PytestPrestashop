import allure
import pytest

from configuration.structions import User
from configuration.ui import UIConfig
from page_objects.registration_page import RegistrationPage


class TestRegistrationPage:
    @allure.id('1')
    @allure.title('Registration - Success')
    def test_success_registration(
            self,
            try_reg_page: RegistrationPage,
            ui_config: UIConfig,
            random_user,
            request: pytest.FixtureRequest
    ):
        user: User = request.cls.user
        allure.dynamic.description("""
        User: {}
        """.format(*user.__dict__))
        try_reg_page.do_registration(
            user.social_title,
            user.first_name,
            user.last_name,
            user.email,
            user.password,
            user.birthday
        )
        try_reg_page.page.check_exact_url(expected_url=ui_config.base_url)
