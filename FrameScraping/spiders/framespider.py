import scrapy
import json
import csv
from scrapy.selector import Selector
class FrameSpider(scrapy.Spider):
  name = "frameScraper"
  start_urls = [
  ]
  def __init__(self):
    self.file = open('frames.json', 'a')
  def parse(self, response):
