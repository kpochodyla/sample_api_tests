import allure
import pytest

from settings.settings import TestSettings


@pytest.fixture(scope="session")
@allure.step("Creating instance of TestSettings")
def settings() -> TestSettings:
    return TestSettings()
