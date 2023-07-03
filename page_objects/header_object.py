from selenium.webdriver import Keys

from locators.header_locators import HeaderLocators
from models.webdriver.driver.element import Element
from models.webdriver.driver.elements import Elements
from models.webdriver.driver.page import Page
from page_factory.dropdown import DropDown
from page_objects.base_page import BasePage


class Header(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header_locators = HeaderLocators(page)


    def get_categories(self) -> Elements:
        items = self.header_locators.dropdowns_items
        items.should_be_visible()
        return items.get_elements()

    def get_subcategories(self) -> Elements:
        items = self.header_locators.dropdowns_sub_items
        return items.get_elements()

    def click_sign_in(self) -> None:
        link = self.header_locators.signin_link
        link.should_be_visible()
        link.click()

    def click_contact_us(self) -> None:
        link = self.header_locators.contact_link
        link.should_be_visible()
        link.click()

    def fill_search(self, text: str) -> None:
        search_input = self.header_locators.search
        search_input.should_be_visible()
        search_input.fill(text)

    def get_search_elements(self) -> Elements:
        """Gets autocomplete items"""
        search_items = self.header_locators.search_result_items
        search_items.should_be_visible()
        return search_items.get_elements()

    def search_smth(self, text: str) -> None:
        self.fill_search(text)
        self.header_locators.search.send_key(Keys.ENTER)

    def get_autocomplete_item(self, text: str) -> Element:
        """
        This function returns a random search element after filling in a search text.

        :param text: A string representing the text to be used for searching and generating autocomplete suggestions
        :type text: str
        :return: a random Element object from a list of search elements that match the given text input.
        """
        self.fill_search(text)
        elements = self.get_search_elements()
        return elements.get_random_element()


    # def get_categories(self) -> Dict[str, DropDown]:
    #     cats = {
    #         "clothes": self.header_locators.clothes_link,
    #         "accessories": self.header_locators.accessories_link,
    #         "art": self.header_locators.art_link
    #     }
    #     return cats
    #
    # def get_subcategories(self) -> Dict[str, Tuple[DropDown]]:
    #     subcats = {
    #         "clothes": (
    #             self.header_locators.men_link,
    #             self.header_locators.woman_link,
    #         ),
    #         'accessories': (
    #             self.header_locators.stationary_link,
    #             self.header_locators.home_accessories_link
    #         )
    #     }
    #     return subcats

    def click_subcategory(self, category: DropDown, subcategory: DropDown):
        category.should_be_visible()
        subcategory.move_to(category.move_to()).click().perform()





    # def get_subcategories(self) -> Elements:
    #     items = self.header_locators.dropdowns_sub_items
    #     items.should_be_visible()
    #     return items.get_elements()

    # def click_category(self, categories: Elements):
    #     for i in range(categories.length()):
    #         cat_list = self.get_categories().get_list()
    #         category = cat_list[i-1]
    #         name = category.text().lower()
    #         category.should().be_clickable()
    #         category.click()

    # def get_category(self) -> Iterable[Element]:
    #     items = self.header_locators.dropdowns_items
    #     items.should_be_visible()
    #     return items.get_one()













