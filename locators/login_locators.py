from models.webdriver.driver.page import Page
from page_factory.button import Button
from page_factory.link import Link


class LoginLocators:
    def __init__(self, page: Page):
        self._page = page

        self.accept_button = Button(
            page,
            locator="#submit-login",
            name="Log in"
        )

        self.show_button = Button(
            page,
            locator=".btn[data-action='show-password']",
            name='Show button'
        )

        self.reset_password_link = Link(
            page,
            locator=".forgot-password a[href*='password-recovery']",
            name="Password recovery link"
        )

        self.registration_link = Link(
            page,
            locator=".no-account a[href*='registration']",
            name="Registration link"
        )
