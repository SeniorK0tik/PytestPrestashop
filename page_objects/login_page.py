from locators.common_locators import PopupsLocators, UserLocators
from locators.login_locators import LoginLocators
from models.webdriver.driver.page import Page
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.common = UserLocators(page)
        self.popups = PopupsLocators(page)
        self.login = LoginLocators(page)

    def do_login(self, email: str, password: str) -> None:
        self.common.email_editor.should_be_visible()
        self.common.email_editor.fill(email)
        self.common.password_editor.should_be_visible()
        self.common.password_editor.fill(password)
        self.login.accept_button.should_be_visible()
        self.login.accept_button.click()

    def get_validation_message(self,  email: str, password: str) -> str:
        self.do_login(email, password)

        if email == '':
            return self.common.email_editor.get_attribute("validationMessage")
        elif password == '':
            return self.common.password_editor.get_attribute("validationMessage")
        else:
            raise ValueError("None of fields are not empty")

    def check_show_password(self) -> None:
        self.common.password_editor.should_be_visible()
        self.common.password_editor.should_have_type(attribute_name='type', attribute_value='password')
        self.login.show_button.should_be_visible()
        self.login.show_button.click()
        self.common.password_editor.should_have_type(attribute_name='type', attribute_value='text')

    def get_popup(self) -> None:
        self.popups.danger_popup.should_be_visible()

    def click_password_recovery(self) -> None:
        self.login.reset_password_link.click()

    def go_to_registration(self) -> None:
        self.login.registration_link.click()
