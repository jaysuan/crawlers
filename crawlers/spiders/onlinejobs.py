# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest


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
        print(f"Response: {response.text}")
        job_posts = response.css('.latest-job-post')
        for job_post in job_posts:
            position = job_post.css('a > dl > dt > h4')
            print(position)
