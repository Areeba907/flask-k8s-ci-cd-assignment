import sys
import os

# Must come BEFORE any other imports that depend on PYTHONPATH
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(repo_root)

from app import home


def test_home():
    assert home() == "Hello, World!"
