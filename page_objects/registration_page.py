import datetime

from pydantic import SecretStr

from configuration.structions import SocialTitle
from locators.common_locators import UserLocators, PopupsLocators
from models.webdriver.driver.page import Page
from page_factory.button import Button
from page_factory.checkbox import Checkbox
from page_factory.link import Link
from page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.user_locators = UserLocators(page)
        self.popups = PopupsLocators(page)

        self.r_button_mr = Button(
            page,
            locator="#field-id_gender-1",
            name="Radio button 'Mr.'"
        )

        self.r_button_mrs = Button(
            page,
            locator="#field-id_gender-2",
            name="Radio button 'Mrs.'"
        )

        self.login_link = Link(
            page,
            locator=".register-form a[href*='login']",
            name="Password recovery link"
        )

        self.registration_link = Link(
            page,
            locator=".no-account a[href*='registration']",
            name="Registration link"
        )

        self.offers_checkbox = Checkbox(
            page,
            locator="input[name='optin']",
            name="Receive offers from our partners"
        )

        self.terms_checkbox = Checkbox(
            page,
            locator="input[name='psgdpr']",
            name="Terms agreement"
        )

        self.newsletter_checkbox = Checkbox(
            page,
            locator="input[name='newsletter']",
            name="Newsletter"
        )

        self.privacy_checkbox = Checkbox(
            page,
            locator="input[name='customer_privacy']",
            name="input[name='customer_privacy']"
        )

        self.save_btn = Button(
            page,
            locator=".btn[data-link-action='save-customer']",
            name="Save"
        )

    def do_registration(
            self,
            social_title: SocialTitle,
            first_name: str,
            last_name: str,
            email: str,
            password: SecretStr,
            birthday: datetime.date,
            offers: bool = True,
            terms: bool = True,
            newsletter: bool = True,
            privacy: bool = True

    ):
        s_titles = {
            "Mr.": self.r_button_mr,
            "Mrs.": self.r_button_mrs
        }
        s_title: Button = s_titles[social_title.value]
        s_title.is_displayed()
        s_title.click()

        self.user_locators.first_name.should_be_visible()
        self.user_locators.first_name.fill(first_name)

        self.user_locators.last_name.should_be_visible()
        self.user_locators.last_name.fill(last_name)

        self.user_locators.email_editor.should_be_visible()
        self.user_locators.email_editor.fill(email)

        self.user_locators.password_editor.should_be_visible()
        self.user_locators.password_editor.fill(password)

        self.user_locators.birthday.should_be_visible()
        self.user_locators.birthday.fill(birthday.strftime("%m/%d/%Y"))

        self.offers_checkbox.is_displayed()
        self.offers_checkbox.click() if offers else None

        self.terms_checkbox.is_displayed()
        self.terms_checkbox.click() if terms else None

        self.newsletter_checkbox.is_displayed()
        self.newsletter_checkbox.click() if newsletter else None

        self.privacy_checkbox.is_displayed()
        self.privacy_checkbox.click() if privacy else None

        self.save_btn.should_be_visible()
        self.save_btn.click()
