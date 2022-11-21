from django.conf import settings
from django.test.runner import DiscoverRunner
from typing import Any

class TestSuiteRunner(DiscoverRunner):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        settings.TEST_MODE = True
        super(TestSuiteRunner, self).__init__(*args, **kwargs)
