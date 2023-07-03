from typing import DefaultDict

import allure
import pytest

from configuration.ui import UIConfig
from page_objects.footer_object import Footer
from tests.footer.conftest import EmailData


class TestFooter:
    @allure.id('1')
    @allure.title('Newsletter Subscription - First Time - Multi time with one email')
    def test_email_subscribed(self, try_footer: Footer, email_footer: EmailData) -> None:
        try_footer.complete_email_form(email_footer.email)
        if email_footer.response == "You have successfully subscribed to this newsletter.":
            try_footer.popups.success_popup.should_have_text(email_footer.response)
        elif email_footer.response == "This email address is already registered.":
            try_footer.popups.danger_popup.should_have_text(email_footer.response)

    @allure.id('2')
    @allure.title('Newsletter input - With no @ - Multi time with one email')
    @pytest.mark.parametrize(
        "input, result", [
            ("kotikmail.ru", "Please include an '@' in the email address. 'kotikmail.ru' is missing an '@'."),
            ("", "Please fill out this field.")
        ]
    )
    def test_email_chars(self, try_footer: Footer, input: str, result: str) -> None:
        try_footer.complete_email_form(input)
        if try_footer.page.webdriver.name == 'firefox':
            if result == "Please include an '@' in the email address. 'kotikmail.ru' is missing an '@'.":
                pytest.xfail(f"FIREFOX does not show correct ValidationMessage: {result}")
        try_footer.footer.email_input.should_have_type("validationMessage", result)

    @allure.id('3')
    @allure.title('PRODUCTS, OUR COMPANY, YOUR ACCOUNT Columns links - Redirect - URLs are expected to be listed')
    def test_first_column(
            self,
            try_footer: Footer,
            columns_schema: DefaultDict[str, str],
            ui_config: UIConfig
    ) -> None:
        columns = [
            try_footer.get_first_column_links,
            try_footer.get_second_column_links,
            try_footer.get_account_links
        ]
        for column in columns:
            c_length = column().length()

            for i in range(c_length):
                els = column().get_list()
                el_text = els[i].text().lower()
                expected_url = ui_config.base_url + columns_schema[el_text]
                el = els[i]
                el.should().be_clickable()
                el.click()
                assert expected_url == try_footer.page.url
                try_footer.page.get_previous_page()
