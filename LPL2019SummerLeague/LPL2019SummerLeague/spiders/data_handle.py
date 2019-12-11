import scrapy  
import bs4
import datetime
import json
from ..items import dataMatchParent

def dateRange(beginDate, endDate):
    dates = []
    dates_return = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    # return dates
    for i in range(len(dates)):
        date_new = dates[i].split("-")
        dates_return.append('%d-%d-%d' % (int(date_new[0]), int(date_new[1]), int(date_new[2])))
    return dates_return
class dataHandle(scrapy.Spider):
	name = 'LPL2019SummerLeague'
	allowed_domain = ['www.scoregg.com']
	
    #循环发送请求，按照分页来理解，就是每页7条数据，一共12页，但是这个有空值情况（没有比赛的时候）
	def start_requests(self):
		all_dates_list=[]
		#因为请求的参数最关键的就是日期参数，我们率先处理日期参数
		dates_list = dateRange("2019-05-27","2019-08-18")
		#将返回的日期参数分组，每组7个
		for k in range(0,len(dates_list),7):
			seven_dates_list = []
			for j in range(k,k+7):
				seven_dates_list.append(dates_list[j])
			all_dates_list.append(seven_dates_list)
		params = {
			"api_path": "services/match/web_math_list.php",
			"gameID": "1",
			"date": "",
			"tournament_id": "120",
			"api_version": "9.9.9",
			"platform": "web"
			}
		for i in range(len(all_dates_list)):
			params["date"]=all_dates_list[i][0]
			print('---------------')
			print(params)
			yield scrapy.FormRequest(
				url = "https://www.scoregg.com/services/api_url.php",
				formdata=params,
				callback=self.parse	
			)
	def parse(self,response):
		print('--------------------')
		data_dic = json.loads(response.text)
		for key in data_dic:
			if len(data_dic[key]!=0):
				info_list=data_dic[key]["info"]["120"]
				match_data_list = info_list['list'][0]

				win_team_id = ""
				match_id = int(match_data_list["match_id"])
				team_id_a = match_data_list["teamID_a"]
				team_id_b = match_data_list['teamID_b']
				team_a_win = match_data_list['team_a_win']
				team_b_win = match_data_list["team_b_win"]
				if int(team_a_win) > int(team_b_win):
					win_team_id = team_id_a
				else:
					win_team_id = team_id_b
				#时间要转换为数据库的datetime格式
				start_date_time_str = match_data_list['start_date']+" "+match_data_list['start_time']
				start_date_time_dt = datetime.datetime.strptime(start_date_time_str,'%Y-%m-%d %H:%M')
				match_attr_id = match_data_list["tournamentID"]

				item_match_p = dataMatchParent()
				item_match_p["match_id"] = match_id
				item_match_p["team_id_a"] = team_id_a
				item_match_p["team_id_b"] = team_id_b
				item_match_p["team_a_win"] = team_a_win
				item_match_p["team_b_win"] = team_b_win
				item_match_p["match_attr_id"] = match_attr_id
				item_match_p["start_date_time"] = start_date_time_dt
				item_match_p["win_team_id"] = win_team_id

				yield item_match_p


