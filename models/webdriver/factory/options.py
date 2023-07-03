from typing import Union

from selenium import webdriver

from models.webdriver.factory.browser import Browser

Options = Union[webdriver.ChromeOptions, webdriver.FirefoxOptions]


def build_options(
    browser: Browser,
    browser_options: Union[list[str], None] = None,
    experimental_options: Union[list[dict], None] = None,
    extension_paths: Union[list[str], None] = None,
) -> Options:
    """Build the Options object for the given browser.

    Args:
        browser: The name of the browser.
        browser_options: The list of options/arguments to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extension filepaths to add to the browser session.

    Usage:
        options = build_options("chrome", ["headless", "incognito"], [{"useAutomationExtension", False}])
    """
    options: Union[Options, None] = None

    if browser == Browser.CHROME:
        options = webdriver.ChromeOptions()
    elif browser == Browser.FIREFOX:
        options = webdriver.FirefoxOptions()
    else:
        raise ValueError(
            f"{browser} is not supported. Cannot build options."
        )

    for option in browser_options:
        normalized_option = option if option.startswith(
            "--") else f"--{option}"
        options.add_argument(normalized_option)

    if experimental_options:
        for exp_option in experimental_options:
            ((name, value),) = exp_option.items()
            options.add_experimental_option(name, value)

    if extension_paths:
        for path in extension_paths:
            options.add_extension(path)

    return options
