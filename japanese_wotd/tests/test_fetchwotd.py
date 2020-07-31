
import os
import sys
import pytest


currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path = [parentdir] + sys.path

import fetch_wotd

def test_module_exists():
    assert os.path.isfile(fetch_wotd.__file__)

@pytest.mark.filterwarnings('ignore::DeprecationWarning')
def test_fetch_word_of_the_day_returns_string():
    result = fetch_wotd.fetch_word_of_the_day()
    assert isinstance(result, str)

def test_get_readme_data_returns_string():
    result = fetch_wotd.get_readme_data()
    assert isinstance(result, str)

def test_word_tag_in_readme():
    result = fetch_wotd.get_readme_data()
    assert fetch_wotd.WORD_TAG in result

def test_can_instantiate_readme_class():
    readme = fetch_wotd.ReadMe()
    assert isinstance(readme, fetch_wotd.ReadMe())