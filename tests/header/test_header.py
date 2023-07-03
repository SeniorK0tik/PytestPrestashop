from typing import DefaultDict

import allure
import pytest

from configuration.ui import UIConfig
from page_objects.header_object import Header


class TestHeader:
    @allure.id('1')
    @allure.title('Main categories - Redirect test - Expect correct url')
    def test_categories_redirect(
            self,
            try_header: Header,
            ui_config: UIConfig,
            categories_schema: DefaultDict[str, str]
    ):
        cats_len = try_header.get_categories().length()
        for i in range(0, cats_len-1):
            elements = try_header.get_categories().get_list()
            element = elements[i]
            name = element.text().lower()
            expected_url = categories_schema[name]
            element.click()
            try_header.page.check_exact_url(expected_url=ui_config.base_url + expected_url)

    @allure.id('2')
    @allure.title('Header sign in redirect - Expect correct url')
    def test_sign_in_(self, try_header: Header, ui_config: UIConfig):
        try_header.click_sign_in()
        regex = "^http:\/\/{base_url}:{port}\/login.*".format(
            base_url=ui_config.base_url.host,
            port=ui_config.base_url.port,
        )
        try_header.page.check_match_url(regex)

    @allure.id('3')
    @allure.title('Header contact us link - Expect correct url')
    def test_contact_us(self, try_header, ui_config: UIConfig):
        try_header.click_contact_us()
        try_header.page.check_exact_url(expected_url=ui_config.base_url + 'contact-us')

    @allure.id('4')
    @allure.title('Search placeholder - Expect correct correct text')
    def test_search_placeholder(self, try_header: Header):
        placeholder = try_header.header_locators.search.get_attribute("placeholder")
        assert placeholder
        assert placeholder == "Search our catalog"

    @allure.id('5')
    @allure.title('Search input')
    @pytest.mark.parametrize(
        "search_input, url_args",
        [("hello", "hello"), ("petka  ", "petka++"), ("kotik usach", "kotik+usach")]
    )
    def test_search_redirect(self, try_header, ui_config: UIConfig, search_input: str, url_args: str):
        try_header.search_smth(search_input)
        try_header.page.check_exact_url(
            expected_url=ui_config.base_url + 'search?controller=search&s=' + url_args
        )

    @pytest.mark.skip
    def test_auto_complete_search(self, try_header):
        raise NotImplemented
