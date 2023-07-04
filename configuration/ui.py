from functools import lru_cache
from typing import Union, Optional, List, Dict

from pydantic import BaseModel, BaseSettings, Field, AnyHttpUrl, EmailStr

from configuration.structions import root_dir
from models.webdriver.factory.browser import Browser
from utils.logger_loguru.logger import logger


class MyBaseSettings(BaseSettings):
    class Config:
        env_file = root_dir.joinpath('.env')
        env_file_encoding = 'utf-8'


class DriverConfig(MyBaseSettings):
    browser: Browser = Field(default=Browser.CHROME, env="BROWSER")
    remote_url: str = Field(default="", env="REMOTE_URL", description="Remote URL to SELENOID")
    wait_time: int = Field(default=10, description="Basic time for Expected Conditions to wait")
    page_load_wait_time: int = 0
    options: list[str] = [
        "ignore-certificate-errors",
        "--no-sandbox",
        "disable-infobars",
        '--headless',
        '--disable-extensions',
        '--disable-gpu'
    ]
    capabilities: dict[str, str] = Field(default={}, description="Local Browser capabilities")
    experimental_options: Union[list[dict], None] = Field(default=None, description="Local Browser capabilities")
    seleniumwire_options: dict = Field(default={}, description="Options for seleniumwire")
    extension_paths: Union[list[str], None] = Field(default=None, description="List of Paths to extensions")
    webdriver_kwargs: Union[dict, None] = Field(default=None, description="Additional arguments for webdriver")
    version: Union[str, None] = Field(default=None, description="Browser version")
    local_path: str = Field(default="", description="Local path to webdriver")


class LoggingConfig(MyBaseSettings):
    log_level: str = "INFO"
    screenshots_on: bool = Field(default=True, env="SCREENSHOTS_ON")
    screenshots_dir: str = Field(
        default='./screenshots', env="SCREENSHOTS_DIR"
    )


class ViewportConfig(BaseModel):
    maximize: bool = True
    width: int = 1440
    height: int = 900
    orientation: str = "portrait"


class DBConfig(MyBaseSettings):
    host: str = Field(default='localhost', env="DB_HOST")
    port: int = Field(default=3306, env="DB_PORT")
    user: str = Field(env="DB_USER", default="prestashop")
    password: Optional[str] = Field(default='', env="DB_PASSWORD")
    db_name: str = Field(env="DB_NAME", default="prestashop")


class PrestaConfig(MyBaseSettings):
    d_u_email: EmailStr = Field(env="DEMO_PRESTA_EMAIL", description="Default user email")
    d_u_password: str = Field(env="DEMO_PRESTA_PASSWORD", description="Default user password")


class AllureConfig(MyBaseSettings):
    url: AnyHttpUrl = Field(env="ALLURE_URL", description="Allure Server URL")
    project_id: str = Field(
        default="default",
        env="ALLURE_PROJECT",
        description="Project ID according to existent projects in your Allure container - "
                    "Check endpoint for project creation >> `[POST]/project"
    )
    results_path: List[str] = Field(
        env="ALLURE_RESULTS",
        description="Sequential list of directories starting from the root of the project"
    )


class RemoteBrowsersConfig(BaseModel):
    browsers: List[Dict] = [
        {
            "browserName": 'chrome',
            "browserVersion": "113.0",
            "selenoid:options": {
                "enableVideo": False
            }
        },
        {
            "browserName": 'firefox',
            "browserVersion": "113.0",
            "selenoid:options": {
                "enableVideo": False
            }
        }
        ]


class UIConfig(MyBaseSettings):
    base_url: AnyHttpUrl = Field(env="BASE_URL", description="Basic URL to main domain")
    driver: DriverConfig = DriverConfig()
    logging: LoggingConfig = LoggingConfig()
    viewport: ViewportConfig = ViewportConfig()
    db: DBConfig = DBConfig()
    presta: PrestaConfig = PrestaConfig()
    allure: AllureConfig = AllureConfig()
    remote_browsers: RemoteBrowsersConfig = RemoteBrowsersConfig()
    custom: dict = {}

    class Config(MyBaseSettings.Config):
        allow_mutation = False


@lru_cache()
def get_ui_config() -> UIConfig:
    return UIConfig()


if __name__ == '__main__':
    conf = UIConfig()
    print(conf.presta.d_u_email)
