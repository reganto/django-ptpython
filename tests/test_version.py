import unittest

from django_ptpython import __version__


class TestVersion(unittest.TestCase):
    def test_django_ptpython_version(self):
        assert __version__ == "1.0.0"
