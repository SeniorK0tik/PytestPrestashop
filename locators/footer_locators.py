from models.webdriver.driver.page import Page
from page_factory.area import Area
from page_factory.button import Button
from page_factory.grid import Grid
from page_factory.input import Input
from page_factory.link import Link


class FooterLocators:
    def __init__(self, page: Page):
        self._page = page

        self.footer_container = Area(
            page,
            locator="#footer",
            name="Footer"
        )

        self.footer_submenu_1 = Area(
            page,
            locator="#footer_sub_menu_1",
            name="Submenu №1"
        )

        self.submenu_1_links = Grid(
            page,
            locator=self.footer_submenu_1 + "a",
            name="Submenu №1 Links"
        )

        self.footer_submenu_2 = Area(
            page,
            locator="#footer_sub_menu_2",
            name="Submenu №2"
        )

        self.submenu_2_links = Grid(
            page,
            locator=self.footer_submenu_2 + "a",
            name="Submenu №2 Links"
        )

        self.account_column = Area(
            page,
            locator=".account-list",
            name="Account column"
        )

        self.account_links = Grid(
            page,
            locator=".account-list a",
            name="Account Links"
        )

        self.contact_infos = Area(
            page,
            locator="#contact-infos",
            name="Contacts"
        )

        self.email_link = Link(
            page,
            locator=self.contact_infos + "a",
            name="Contact Email"
        )

        self.email_input = Input(
            page,
            locator=self.footer_container + "input[name='email']",
            name="Footer Email"
        )

        self.subscribe_btn = Button(
            page,
            locator=self.footer_container + "input[name='submitNewsletter']",
            name="Submit Newsletter"
        )
