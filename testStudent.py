# import numpy as np
# import time 
# print(dir(np))
import os
# print(' 的实际时长为：{:.2f}分钟,{}\n'.format(10/60,10))
# start_time = time.time()
# time.sleep(9)
# actual_time = start_time - time.time()
# print(actual_time)


# to_addr_list = ["rejrot6rln@qq.com","897779411@qq.com","546040890@qq.com","386709279@qq.com","1324629332@qq.com","757195339@qq.com"]
# for i in range(len(to_addr_list)):
# 	print(to_addr_list[i])

# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# use_image_name = ['bdyjy.jpg', 'jzmb.jpg']
# for i in range(len(use_image_name)):
# 	print("attachment; filename='ny:{}'".format(use_image_name[i]))

# message = MIMEMultipart()

# print(type(message))

# use_image_name = ['bdyjy.jpg', 'jzmb.jpg']
# for i in range(len(use_image_name)):
# 	print("image/{}".format(use_image_name[i]))
# #附件处理

# for i in range(len(use_image_name)):
# 	att = MIMEText(open("image/{}".format(use_image_name[i]), 'rb').read(), 'base64', 'utf-8')
# 	att["Content-Type"] = 'application/octet-stream'
# 	att["Content-Disposition"] = "attachment; filename='ny:{}'".format(use_image_name[i])
# 	message.attach(att)
# print(message)
# import MyQR
# from MyQR import myqr

# print(dir(myqr))
# myqr.run(words='https://www.baidu.com',picture='image/pkq.jpg',save_name='image/qr.png',colorized=True)
# unit_rooms={ 3:{301:[1,80],302:[1,80],303:[2,90],304:[2,90]},
#              4:{401:[1,80],402:[1,80],403:[2,90],404:[2,90]},
#              5:{501:[1,80],502:[1,80],503:[2,90],504:[2,90]}
#             }
# for key in unit_rooms:
# 	for map_key in unit_rooms[key]:
# 		print("房间号{},朝向{}面积{}".format(map_key,unit_rooms[key][map_key][0],unit_rooms[key][map_key][1]))
# import requests
# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md') 
# # novel = res.text

# # with open("TESTdoc/novel.txt","w",encoding="utf-8") as novel_file:
# # 	novel_file.write(novel[:100])
# # print("End!!!")

# print(dir(res))

# f1 = open("TESTdoc/test.txt","a",encoding = "utf-8")
# print(type(f1))
# f1.write("难念的经")
# print(type(f1.write("333")))
# f1.close()
# f2 = open("TESTdoc/test.txt","r",encoding = "utf-8")
# print(f2.read())
# f2.close()
# dirPath = "TESTdoc/"
# if(os.path.exists(dirPath+"movie-info.csv")):
# 	os.remove(dirPath+"movie-info.csv")
# else:
# 	print("要删除的文件不存在！！！")
# import requests
# # 引用requests库
# res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# # 调用get方法，下载这个字典
# json_music = res_music.json()
# # 使用json()方法，将response对象，转为列表/字典
# list_music = json_music['data']['song']['list']
# print(json_music)
# 一层一层地取字典，获取歌单列表
# for music in list_music:
# # list_music是一个列表，music是它里面的元素
#     print(music['name'])
#     # 以name为键，查找歌曲名

# from string import digits
# s = 'abc3def4456ghi789zero0'
# print(digits)
# remove_digits = str.maketrans('', '', digits)
# print(remove_digits)
# print(type(remove_digits))
# res = s.translate(remove_digits)
# print(res)
# transtab = str.maketrans({'a':'b'})
# news = 'apple'
# print (news.translate(transtab))

# print("-------------------------")

# transtab = str.maketrans('ap','bs')
# news = 'apple'
# print (news.translate(transtab))

# print("-------------------------")

# transtab = str.maketrans('','','al')
# print(transtab)
# news = 'apple'
# print (news.translate(transtab))
# dictt = {1:"a",2:"3"}
# dictt[44] = "bb"
# print(dictt)
# from selenium import webdriver
# print(dir(webdriver))
import requests
# res = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md")
# with open("TESTdoc/test1.txt","w") as file:
# 	file.write(res.text)
# print("OK")
# res = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md")
# print(dir(res))
# print(type(res.content.decode("utf-8")))
# res = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md")
# with open("TESTdoc/test2.txt","w") as file:
#  	file.write(res.content.decode("utf-8"))
# print("OK")
# file1 = open("TESTdoc/test3.txt","wb")
# content = res.content
# file1.write(content)
# file1.close()
# from urllib import parse
# str1 = '天津'
# str2 = parse.quote(str1)   #quote()将字符串进行编码
# print(str2) 

# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--no-sandbox");#划重点,加上这句,就不会报崩溃了,当然也可能是chromedriver和chrome的版本匹配问题
# driver = webdriver.Chrome()
#https://localprod.pandateacher.com/python-manuscript/hello-spiderman/
# driver.get("https://localprod.pandateacher.com/python-manuscript/hello-spiderman/")
# driver.get('http://www.baidu.com/')
# time.sleep(4)
# teacher = driver.find_element_by_id("teacher")
# assistant = driver.find_element_by_id("assistant")
# sub_btn = driver.find_element_by_class_name("sub")

# teacher.send_keys("吴枫")
# assistant.send_keys("延君")
# sub_btn.click()

# time.sleep(4)

# print(type(teacher))


# def gen_func():
#     html = yield 'http://www.baidu.com' # yield 前面加=号就实现了1：可以产出值2：可以接受调用者传过来的值
#     print(html)
#     yield 2
#     yield 3
#     return 'bobby'
# if __name__ == '__main__':
#     gen = gen_func()
#     url = next(gen)
#     print(url)
#     html = 'bobby'
#     gen.send(html) # send方法既可以将值传递进生成器内部，又可以重新启动生成器执行到下一yield位置。
#---------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
from xpinyin import Pinyin
import json
# post_name = input("Please Input Post Company Name:").strip("")
# post_id = input("Please Input Post_id:").strip("")
# pin = Pinyin()
# post_name_pinyin = pin.get_pinyin(post_name).replace("-","")
headers =  {
	'Origin':'www.scoregg.com',
	# 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
	'Referer':"https://www.scoregg.com/data/hero",
	# 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36S',
	    # 标记了请求从什么设备，什么浏览器上发出
	}

post_url = "https://www.scoregg.com/services/api_url.php"
post_params = {
	"api_path": "services/match/web_math_list.php",
	"gameID": "1",
	"date": "2019-5-27",
	"tournament_id": "120",
	"api_version": "9.9.9",
	"platform": "web"
	}
r = requests.post(post_url, post_params)
        #post需要输入两个参数，一个是刚才的链接，一个是data，返回的是一个Response对象
answer=json.loads(r.text,strict=False)
print(answer["data"]["list"])
strdate  = "2019-8-8"
strdatec = strdate.split("-")
strdatec1 = []
print(strdatec)
for i in range(len(strdatec)):
	if i >0 and int(strdatec[i])<10:
		strdatec[i] = "0{}".format(strdatec[i])
	strdatec1.append(strdatec[i])
print(strdatec1)
print("%s.%s.%s" % (int(strdatec1[0]), strdatec1[1], strdatec1[2]))
# print(answer["data"]["list"]["2019.07.15"])
# print(answer["data"]["list"]["2019.07.16"])
#----------------------------------------------------------------------
# str_1='https://img1.famulei.com/common/images/champion/Lux.png'
# char_1="/"
# index_list=[]
# count=0
# str_list=list(str_1)
# for each_char in str_list:
#  count+=1
#  if each_char==char_1:
#   index_list.append((count-1))
#   print(each_char,count-1)
# print(index_list[-1])、
#-------------------------------------------------------------------------------------
#BanPick
# def indexNum(str1="",chr=""):
# 	index_list = []
# 	count = 0
# 	str_list = list(str1)
# 	for each_char in str_list:
# 		count+=1
# 		if each_char == chr:
# 			index_list.append((count-1))
# 	return index_list[-1]
# print(indexNum("https://img1.famulei.com/common/images/champion/Lux.png","/"))
# print(indexNum("https://img1.famulei.com/common/images/champion/Lux.png","."))
# str = "https://img1.famulei.com/common/images/champion/Lux.png"
# print(str[47+1:51])
