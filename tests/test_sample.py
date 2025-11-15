import os
import sys

# Add project root to Python path BEFORE importing app
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

from app import home   # <-- MUST be after sys.path modification


def test_home():
    assert home() == "Hello, World!"
