# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.loader import ItemLoader

from crawlers.items import Job


class OnlinejobsSpider(scrapy.Spider):
    name = 'onlinejobs'
    allowed_domains = ['onlinejobs.ph']

    def start_requests(self):
        categories = [('Software Development', '2')]
        url = 'https://www.onlinejobs.ph/jobseekers/jobsearch'
        for category in categories:
            yield FormRequest(url=url,
            formdata={
                "jobcat": category[1],
                "Freelance": 'on',
                "partTime": 'on',
                "fullTime": 'on'
            })

    def parse(self, response):
        job_posts = response.css('.latest-job-post')
        for job_post in job_posts:
            loader = ItemLoader(item=Job(), selector=job_post)
            loader.add_css('position', 'h4::text')
            loader.add_css('job_type', 'h4 > span::text')
            loader.add_css('link', 'a::attr(href)')
            yield loader.load_item()
