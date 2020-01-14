# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item
from scrapy.loader.processors import Join, MapCompose, TakeFirst


def filter_empty_strings(item):
    return None if item.isspace() else item

class Job(Item):
    position = Field(
        input_processor=MapCompose(filter_empty_strings, str.strip),
        output_processor=Join()
    )
    job_type = Field(output_processor=TakeFirst())
    link = Field(output_processor=TakeFirst())