from locators.common_locators import PopupsLocators
from locators.footer_locators import FooterLocators
from models.webdriver.driver.elements import Elements
from models.webdriver.driver.page import Page
from page_objects.base_page import BasePage


class Footer(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.popups = PopupsLocators(page)
        self.footer = FooterLocators(page)

    def get_first_column_links(self) -> Elements:
        self.footer.submenu_1_links.should_be_visible()
        return self.footer.submenu_1_links.get_elements()

    def get_second_column_links(self) -> Elements:
        self.footer.submenu_2_links.should_be_visible()
        return self.footer.submenu_2_links.get_elements()

    def get_account_links(self) -> Elements:
        self.footer.account_links.should_be_visible()
        return self.footer.account_links.get_elements()

    def complete_email_form(self, email: str):
        # self.footer.email_input.move_to().perform()
        self.footer.email_input.should_be_visible()
        self.footer.email_input.fill(value=email)
        self.footer.subscribe_btn.should_be_visible()
        self.footer.subscribe_btn.click()
