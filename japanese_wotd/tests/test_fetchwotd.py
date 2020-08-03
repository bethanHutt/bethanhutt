
import os
import sys
import pytest


currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path = [parentdir] + sys.path

import fetch_wotd

@pytest.fixture(scope='module')
def new_wotd():
    new_wotd = fetch_wotd.fetch_word_of_the_day()
    return new_wotd

@pytest.fixture(scope='module')
def readme():
    readme = fetch_wotd.ReadMe()
    return readme

def test_module_exists():
    assert os.path.isfile(fetch_wotd.__file__)

@pytest.mark.filterwarnings('ignore::DeprecationWarning')
def test_fetch_word_of_the_day_returns_string(new_wotd):
    assert isinstance(new_wotd, str)

def test_get_readme_data_returns_string(readme):
    result = readme.get_readme_data()
    assert isinstance(result, str)

def test_word_tag_in_readme(readme):
    result = readme.get_readme_data()
    assert fetch_wotd.WOTD_TAG in result

def test_can_instantiate_readme_class():
    readme = fetch_wotd.ReadMe()
    assert isinstance(readme, fetch_wotd.ReadMe)

def test_new_wotd_in_new_readme(new_wotd, readme):
    readme.replace_word_of_the_day(new_wotd=new_wotd)
    assert new_wotd in readme.new_readme