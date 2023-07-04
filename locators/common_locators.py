from models.webdriver.driver.page import Page
from page_factory.editor import Editor
from page_factory.input import Input
from page_factory.popup import Popup


class PopupsLocators:
    def __init__(self, page: Page):
        self._page = page

        self.danger_popup = Popup(
            page,
            locator=".alert-danger",
            name='Fail indicator'
        )

        self.success_popup = Popup(
            page,
            locator=".alert-success",
            name="Success indicator"
        )


class UserLocators:
    def __init__(self, page: Page):
        self._page = page

        self.first_name = Input(
            page,
            locator="#field-firstname",
            name="First name"
        )

        self.last_name = Input(
            page,
            locator="#field-lastname",
            name="Last Name"
        )

        self.birthday = Input(
            page,
            locator="#field-birthday",
            name="Birthday"
        )

        self.email_editor = Editor(
            page,
            locator="#field-email",
            name="Email editor"
        )

        self.password_editor = Editor(
            page,
            locator="#field-password",
            name="Password editor"
        )
