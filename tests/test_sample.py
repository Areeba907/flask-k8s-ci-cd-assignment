import sys
import os

# Add repo root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import home


def test_home():
    assert home() == "Hello, World!"
