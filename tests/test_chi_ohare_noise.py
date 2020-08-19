from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.chi_ohare_noise import ChiOhareNoiseSpider

test_response = file_response(
    join(dirname(__file__), "files/chi_ohare_noise", "chi_ohare_noise.html"),
    url="https://www.oharenoise.org/about-oncc/agendas-and-minutes",
)
spider = ChiOhareNoiseSpider()

freezer = freeze_time("2020-07-09")
freezer.start()

parsed_items = [item for item in spider.ChiOhareNoiseSubSpider1().parse(test_response)]

freezer.stop()


def test_tests():
    print("here")
    assert len(parsed_items) == 45


"""
Uncomment below
"""

#def test_title():
    #assert parsed_items[0]["title"] == "EXPECTED TITLE"


# def test_description():
#     assert parsed_items[0]["description"] == "EXPECTED DESCRIPTION"


# def test_start():
#     assert parsed_items[0]["start"] == datetime(2019, 1, 1, 0, 0)


# def test_end():
#     assert parsed_items[0]["end"] == datetime(2019, 1, 1, 0, 0)


# def test_time_notes():
#     assert parsed_items[0]["time_notes"] == "EXPECTED TIME NOTES"


# def test_id():
#     assert parsed_items[0]["id"] == "EXPECTED ID"


# def test_status():
#     assert parsed_items[0]["status"] == "EXPECTED STATUS"


# def test_location():
#     assert parsed_items[0]["location"] == {
#         "name": "EXPECTED NAME",
#         "address": "EXPECTED ADDRESS"
#     }


# def test_source():
#     assert parsed_items[0]["source"] == "EXPECTED URL"


# def test_links():
#     assert parsed_items[0]["links"] == [{
#       "href": "EXPECTED HREF",
#       "title": "EXPECTED TITLE"
#     }]


# def test_classification():
#     assert parsed_items[0]["classification"] == NOT_CLASSIFIED


# @pytest.mark.parametrize("item", parsed_items)
# def test_all_day(item):
#     assert item["all_day"] is False
