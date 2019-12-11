# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import match_p_items

class Lpl2019SummerleaguePipeline(object):
	def __init__(self):
		self.db=pymysql.connect()
		self.cur=self.db.cursor()
	def process_item(self, item, spider):
		if isinstance(item,match_p_items.dataMatchParent):
			sql='INSERT INTO match_parent(id,team_id_a,team_id_b,start_date_time,team_a_win,team_b_win,win_team_id,match_attr_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
			self.cur.execute(sql,(item['match_id'],item['team_id_a'],item['team_id_b'],item['start_date_time'],item['team_a_win'],item['team_b_win'],item['win_team_id'],item['match_attr_id']))
			self.db.commit()
		return item
