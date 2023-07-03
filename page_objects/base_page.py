from typing import Iterable

import allure
from seleniumwire.request import Response

from models.webdriver.driver.page import Page



class BasePage:
    def __init__(self, page: Page) -> None:
        self._page = page
        # self.cookies_modal = CookiesModal(page)

    @property
    def page(self) -> Page:
        return self._page

    def visit(self, url: str) -> None:
        with allure.step(f'Opening the url "{url}"'):
            self._page.visit(url)
            # self.cookies_modal.accept_cookies()

    def get_page_responses(self) -> Iterable[Response]:
        with allure.step(f'Getting page responses with "{self.page.url}"'):
            return self._page.webdriver.requests

    def reload(self) -> Page:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self._page.reload()

    def delete_all_cookies(self) -> None:
        with allure.step('Delete all page cookies'):
            self._page.delete_all_cookies()

    def reverse_page(self) -> Page:
        with allure.step("Go back to previous page"):
            return self._page.get_previous_page()

    @property
    def get_page(self) -> Page:
        return self._page
