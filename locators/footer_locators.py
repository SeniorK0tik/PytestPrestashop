from locators.base import Locator
from models.webdriver.driver.page import Page
from page_factory.area import Area
from page_factory.button import Button
from page_factory.grid import Grid
from page_factory.input import Input
from page_factory.link import Link


class fff(Locator):
    footer = {"css": "#footer"}
    newsletter_block = {"css": footer['css'] + " .block_newsletter"}
    newsletter_label = {"css": newsletter_block["css"] + " #block-newsletter-label"}
    email_input = {"css": newsletter_block["css"] + " input[name='email']"}
    subscribe_btn = {"css": newsletter_block["css"] + " .btn[value='Subscribe']"}

    footer_container = {"css": footer['css'] + " .footer-container"}
    # footer_sub_menu = {"css": footer_container['css': " ul[id*='footer_sub_menu']"]}

    block_myaccount_infos = {"css": footer_container['css'] + " #block_myaccount_infos"}

    block_contact = {"css":  footer_container['css'] + " div[class*='block-contact']"}

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