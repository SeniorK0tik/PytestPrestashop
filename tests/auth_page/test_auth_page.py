import allure
import pytest
from configuration.ui import UIConfig
from page_objects.login_page import LoginPage


class TestAuthPage:
    @allure.id('1')
    @allure.title('Auth page responses')
    @allure.description('Selenium wire option to test response codes')
    @pytest.mark.skip
    def test_auth_page_responses(self, try_login_page: LoginPage):
        responses = try_login_page.get_page_responses()
        for res in responses:
            assert res.response.status_code == 200

    @allure.id('2')
    @allure.title('Login - Success')
    def test_success_login(
            self,
            try_login_page: LoginPage,
            ui_config: UIConfig
    ):
        try_login_page.do_login(email=ui_config.presta.d_u_email, password=ui_config.presta.d_u_password)
        try_login_page.page.check_exact_url(expected_url=ui_config.base_url)

    @allure.id('3')
    @allure.title('Login - Fail - Not filled field')
    def test_not_filled_fields(
            self,
            try_login_page: LoginPage,
            ui_config: UIConfig,
            user_data_comb_with_empty_field,
    ):
        ms = try_login_page.get_validation_message(*user_data_comb_with_empty_field)
        assert ms == "Please fill out this field."

    @allure.id('4')
    @allure.title('Login - Fail - Incorrect data')
    def test_fail_login(self, try_login_page: LoginPage, user_data_comb):
        try_login_page.do_login(*user_data_comb)
        try_login_page.get_popup()

    @allure.id('5')
    @allure.title('Show Password Try')
    def test_show_pas_btn(self, try_login_page: LoginPage):
        try_login_page.check_show_password()

    @allure.id('6')
    @allure.title('Reset Password Link - Redirect')
    def test_reset_password_link(self, try_login_page: LoginPage, ui_config: UIConfig):
        try_login_page.click_password_recovery()
        try_login_page.page.check_exact_url(expected_url=ui_config.base_url + "password-recovery")

    @allure.id('7')
    @allure.title('Registration Link - Redirect')
    @pytest.mark.xfail(reason='Prestashop 1.7 does not have path /registration')
    def test_registration_link(self, try_login_page: LoginPage, ui_config: UIConfig):
        try_login_page.go_to_registration()
        try_login_page.page.check_exact_url(expected_url=ui_config.base_url + "registration")
