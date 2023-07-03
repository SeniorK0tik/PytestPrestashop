from typing import Iterable

import allure

from models.webdriver.driver.element import Element
from page_factory.component import Component


class Grid(Component):
    @property
    def type_of(self) -> str:
        return 'grid'



    # def get_one(self) -> Iterable[Element]:
    #     """Gets one Element from Grid"""
    #     elements = self.get_elements().get_list()
    #     for el in elements:
    #         yield el
