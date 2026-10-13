import pytest
from tests.fixtures.app import *
from tests.fixtures.forum import *
from tests.fixtures.user import *


@pytest.fixture(scope="package")
def tested_plugins():
    """The test app blocks every plugin except the ones listed here."""
    return ["{{ cookiecutter.plugin_module }}"]
