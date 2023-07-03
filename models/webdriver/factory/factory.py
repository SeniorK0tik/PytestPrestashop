from selenium.webdriver.remote.webdriver import WebDriver

from configuration.ui import UIConfig
from models.webdriver.factory.browser import Browser
from models.webdriver.factory.builders import build_remote, build_chrome, build_firefox


def build_from_config(config: UIConfig) -> WebDriver:
    """
    The "main" method for building a WebDriver using UIConfig.
    Args:
        config: UIConfig from config.py
    Usage:
        driver = webdriver_factory.build_from_config(config)
    Returns:
        An instance of WebDriver.
    """
    browser = config.driver.browser
    remote_url = config.driver.remote_url

    build_config = {
        "options": config.driver.options,
        "capabilities": config.driver.capabilities,
        "experimental_options": config.driver.experimental_options,
        "extension_paths": config.driver.extension_paths,
        "webdriver_kwargs": config.driver.webdriver_kwargs
    }

    if remote_url:
        return build_remote(remote_url, **build_config)

    # Start with SeleniumWire drivers
    # Set fields for the rest of the non-remote drivers
    build_config["version"] = config.driver.version
    build_config["local_path"] = config.driver.local_path


    if browser == Browser.CHROME:
        return build_chrome(
            seleniumwire_options=config.driver.seleniumwire_options, **build_config
        )
    elif browser == Browser.FIREFOX:
            return build_firefox(
                seleniumwire_options=config.driver.seleniumwire_options, **build_config
            )
    else:
        raise ValueError(
            f"{config.driver.browser} is not supported. Cannot build WebDriver from config."
        )
