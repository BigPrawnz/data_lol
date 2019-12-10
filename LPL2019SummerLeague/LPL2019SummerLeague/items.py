# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lpl2019SummerleagueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class dataMatchParent(scrapy.Item):
	match_id = scrapy.Field()
	team_id_a = scrapy.Field()
	team_id_b = scrapy.Field()
	start_date_time = scrapy.Field()
	team_a_win = scrapy.Field()
	team_b_win = scrapy.Field()
	win_team_id = scrapy.Field()
class dataMatches(scrapy.Item):
	pass
class dataBan(scrapy.Item):
	pass
class dataPick(scrapy.Item):
	pass