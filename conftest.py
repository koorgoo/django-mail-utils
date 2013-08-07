import os
import sys


def pytest_configure():
    curdir = os.path.dirname(__file__)
    sys.path.append(curdir)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')
