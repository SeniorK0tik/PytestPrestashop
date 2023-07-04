from models.webdriver.driver.page import Page
from page_factory.area import Area
from page_factory.dropdown import DropDown
from page_factory.grid import Grid
from page_factory.input import Input
from page_factory.link import Link


class HeaderLocators:
    def __init__(self, page: Page):
        self._page = page

        self._header = Area(
            page,
            locator="#header",
            name="Header"
        )

        self.signin_link = Link(
            page,
            locator=".user-info a",
            name="Sign in link"
        )

        self.cart_block = Area(
            page,
            locator=".blockcart",
            name="Blockcart"
        )

        self.cart_link = Link(
            page,
            locator=self.cart_block + "a",
            name="Cart"
        )

        self.search = Input(
            page,
            locator="#search_widget input[class='ui-autocomplete-input']",
            name="Search input"
        )

        self.search_result_items = Grid(
            page,
            locator=".ui-menu-item",
            name="Search result"
        )

        self.categories_area = Area(
            page,
            locator=".top-menu[id='top-menu']",
            name="Categories"
        )

        self.contact_link = Link(
            page,
            locator=self._header + "a[href*='contact-us']",
            name="Contact us"
        )

        self.logo_link = Link(
            page,
            locator=self._header + "a:has(img.logo)",
            name="Logo"
        )

        self.categories = Grid(
            page,
            locator=self.categories_area + "li[class='category']",
            name="Categories"
        )

        self.dropdowns_items = Grid(
            page,
            locator=self.categories + "a[class='dropdown-item']",
            name="Categories-items"
        )

        self.dropdowns_sub_items = Grid(
            page,
            locator=self.categories + "a[class*='dropdown-submenu']",
            name="Categories-sub_items"
        )

        self.clothes_link = DropDown(
            page,
            locator="#category-3>a",
            name="Clothes category"
        )

        self.accessories_link = DropDown(
            page,
            locator="#category-6>a",
            name="Accessories category"
        )

        self.art_link = DropDown(
            page,
            locator="#category-9>a",
            name="Art category"
        )

        self.men_link = DropDown(
            page,
            locator="#category-4>a",
            name="Man category"
        )

        self.woman_link = DropDown(
            page,
            locator="#category-5>a",
            name="Woman category"
        )

        self.stationary_link = DropDown(
            page,
            locator="#category-7>a",
            name="Stationary category"
        )

        self.home_accessories_link = DropDown(
            page,
            locator="#category-7>a",
            name="Home accessories category"
        )
